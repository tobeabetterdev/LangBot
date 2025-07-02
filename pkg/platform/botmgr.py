from __future__ import annotations

import sys
import asyncio
import traceback
import sqlalchemy

#     FriendMessage, Image, MessageChain, Plain
from . import adapter as msadapter

from ..core import app, entities as core_entities, taskmgr
from .types import events as platform_events, message as platform_message

from ..discover import engine

from ..entity.persistence import bot as persistence_bot

from ..entity.errors import platform as platform_errors

from .logger import EventLogger

# 处理 3.4 移除了 YiriMirai 之后，插件的兼容性问题
from . import types as mirai

sys.modules['mirai'] = mirai


class RuntimeBot:
    """运行时机器人"""

    ap: app.Application

    bot_entity: persistence_bot.Bot

    enable: bool

    adapter: msadapter.MessagePlatformAdapter

    task_wrapper: taskmgr.TaskWrapper

    task_context: taskmgr.TaskContext

    logger: EventLogger

    def __init__(
        self,
        ap: app.Application,
        bot_entity: persistence_bot.Bot,
        adapter: msadapter.MessagePlatformAdapter,
        logger: EventLogger,
    ):
        self.ap = ap
        self.bot_entity = bot_entity
        self.enable = bot_entity.enable
        self.adapter = adapter
        self.task_context = taskmgr.TaskContext()
        self.logger = logger

    async def initialize(self):
        async def on_friend_message(
            event: platform_events.FriendMessage,
            adapter: msadapter.MessagePlatformAdapter,
        ):
            image_components = [
                component for component in event.message_chain if isinstance(component, platform_message.Image)
            ]

            await self.logger.info(
                f'{event.message_chain}',
                images=image_components,
                message_session_id=f'person_{event.sender.id}',
            )

            await self.ap.query_pool.add_query(
                bot_uuid=self.bot_entity.uuid,
                launcher_type=core_entities.LauncherTypes.PERSON,
                launcher_id=event.sender.id,
                sender_id=event.sender.id,
                message_event=event,
                message_chain=event.message_chain,
                adapter=adapter,
                pipeline_uuid=self.bot_entity.use_pipeline_uuid,
            )

        async def on_group_message(
            event: platform_events.GroupMessage,
            adapter: msadapter.MessagePlatformAdapter,
        ):
            image_components = [
                component for component in event.message_chain if isinstance(component, platform_message.Image)
            ]

            await self.logger.info(
                f'{event.message_chain}',
                images=image_components,
                message_session_id=f'group_{event.group.id}',
            )

            await self.ap.query_pool.add_query(
                bot_uuid=self.bot_entity.uuid,
                launcher_type=core_entities.LauncherTypes.GROUP,
                launcher_id=event.group.id,
                sender_id=event.sender.id,
                message_event=event,
                message_chain=event.message_chain,
                adapter=adapter,
                pipeline_uuid=self.bot_entity.use_pipeline_uuid,
            )

        self.adapter.register_listener(platform_events.FriendMessage, on_friend_message)
        self.adapter.register_listener(platform_events.GroupMessage, on_group_message)

    async def run(self):
        async def exception_wrapper():
            try:
                self.task_context.set_current_action('Running...')
                await self.adapter.run_async()
                self.task_context.set_current_action('Exited.')
            except Exception as e:
                if isinstance(e, asyncio.CancelledError):
                    self.task_context.set_current_action('Exited.')
                    return
                self.task_context.set_current_action('Exited with error.')
                await self.logger.error(f'平台适配器运行出错:\n{e}\n{traceback.format_exc()}')

        self.task_wrapper = self.ap.task_mgr.create_task(
            exception_wrapper(),
            kind='platform-adapter',
            name=f'platform-adapter-{self.adapter.__class__.__name__}',
            context=self.task_context,
            scopes=[
                core_entities.LifecycleControlScope.APPLICATION,
                core_entities.LifecycleControlScope.PLATFORM,
            ],
        )

    async def shutdown(self):
        await self.adapter.kill()

        self.ap.task_mgr.cancel_task(self.task_wrapper.id)


# 控制QQ消息输入输出的类
class PlatformManager:
    # ====== 4.0 ======
    ap: app.Application = None

    bots: list[RuntimeBot]

    webchat_proxy_bot: RuntimeBot

    adapter_components: list[engine.Component]

    adapter_dict: dict[str, type[msadapter.MessagePlatformAdapter]]

    def __init__(self, ap: app.Application = None):
        self.ap = ap
        self.bots = []
        self.adapter_components = []
        self.adapter_dict = {}

    async def initialize(self):
        self.adapter_components = self.ap.discover.get_components_by_kind('MessagePlatformAdapter')
        adapter_dict: dict[str, type[msadapter.MessagePlatformAdapter]] = {}
        for component in self.adapter_components:
            adapter_dict[component.metadata.name] = component.get_python_component_class()
        self.adapter_dict = adapter_dict

        webchat_adapter_class = self.adapter_dict['webchat']

        # initialize webchat adapter
        webchat_logger = EventLogger(name='webchat-adapter', ap=self.ap)
        webchat_adapter_inst = webchat_adapter_class(
            {},
            self.ap,
            webchat_logger,
        )

        self.webchat_proxy_bot = RuntimeBot(
            ap=self.ap,
            bot_entity=persistence_bot.Bot(
                uuid='webchat-proxy-bot',
                name='WebChat',
                description='',
                adapter='webchat',
                adapter_config={},
                enable=True,
            ),
            adapter=webchat_adapter_inst,
            logger=webchat_logger,
        )
        await self.webchat_proxy_bot.initialize()

        await self.load_bots_from_db()

    def get_running_adapters(self) -> list[msadapter.MessagePlatformAdapter]:
        return [bot.adapter for bot in self.bots if bot.enable]

    async def load_bots_from_db(self):
        self.ap.logger.info('Loading bots from db...')

        self.bots = []

        result = await self.ap.persistence_mgr.execute_async(sqlalchemy.select(persistence_bot.Bot))

        bots = result.all()

        for bot in bots:
            # load all bots here, enable or disable will be handled in runtime
            try:
                await self.load_bot(bot)
            except platform_errors.AdapterNotFoundError as e:
                self.ap.logger.warning(f'Adapter {e.adapter_name} not found, skipping bot {bot.uuid}')
            except Exception as e:
                self.ap.logger.error(f'Failed to load bot {bot.uuid}: {e}\n{traceback.format_exc()}')

    async def load_bot(
        self,
        bot_entity: persistence_bot.Bot | sqlalchemy.Row[persistence_bot.Bot] | dict,
    ) -> RuntimeBot:
        """加载机器人"""
        if isinstance(bot_entity, sqlalchemy.Row):
            bot_entity = persistence_bot.Bot(**bot_entity._mapping)
        elif isinstance(bot_entity, dict):
            bot_entity = persistence_bot.Bot(**bot_entity)

        logger = EventLogger(name=f'platform-adapter-{bot_entity.name}', ap=self.ap)

        if bot_entity.adapter not in self.adapter_dict:
            raise platform_errors.AdapterNotFoundError(bot_entity.adapter)

        adapter_inst = self.adapter_dict[bot_entity.adapter](
            bot_entity.adapter_config,
            self.ap,
            logger,
        )

        runtime_bot = RuntimeBot(ap=self.ap, bot_entity=bot_entity, adapter=adapter_inst, logger=logger)

        await runtime_bot.initialize()

        self.bots.append(runtime_bot)

        return runtime_bot

    async def get_bot_by_uuid(self, bot_uuid: str) -> RuntimeBot | None:
        for bot in self.bots:
            if bot.bot_entity.uuid == bot_uuid:
                return bot
        return None

    async def remove_bot(self, bot_uuid: str):
        for bot in self.bots:
            if bot.bot_entity.uuid == bot_uuid:
                if bot.enable:
                    await bot.shutdown()
                self.bots.remove(bot)
                return

    def get_available_adapters_info(self) -> list[dict]:
        return [
            component.to_plain_dict() for component in self.adapter_components if component.metadata.name != 'webchat'
        ]

    def get_available_adapter_info_by_name(self, name: str) -> dict | None:
        for component in self.adapter_components:
            if component.metadata.name == name:
                return component.to_plain_dict()
        return None

    def get_available_adapter_manifest_by_name(self, name: str) -> engine.Component | None:
        for component in self.adapter_components:
            if component.metadata.name == name:
                return component
        return None

    async def write_back_config(
        self,
        adapter_name: str,
        adapter_inst: msadapter.MessagePlatformAdapter,
        config: dict,
    ):
        # index = -2

        # for i, adapter in enumerate(self.adapters):
        #     if adapter == adapter_inst:
        #         index = i
        #         break

        # if index == -2:
        #     raise Exception('平台适配器未找到')

        # # 只修改启用的适配器
        # real_index = -1

        # for i, adapter in enumerate(self.ap.platform_cfg.data['platform-adapters']):
        #     if adapter['enable']:
        #         index -= 1
        #         if index == -1:
        #             real_index = i
        #             break

        # new_cfg = {
        #     'adapter': adapter_name,
        #     'enable': True,
        #     **config
        # }
        # self.ap.platform_cfg.data['platform-adapters'][real_index] = new_cfg
        # await self.ap.platform_cfg.dump_config()

        # TODO implement this
        pass

    async def run(self):
        # This method will only be called when the application launching
        await self.webchat_proxy_bot.run()

        for bot in self.bots:
            if bot.enable:
                await bot.run()

    async def shutdown(self):
        for bot in self.bots:
            if bot.enable:
                await bot.shutdown()
        self.ap.task_mgr.cancel_by_scope(core_entities.LifecycleControlScope.PLATFORM)
