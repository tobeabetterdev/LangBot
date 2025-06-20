from __future__ import annotations
import copy
import pickle

from ...core import entities as core_entities
from . import handler
from .handlers import chat, command
from .. import entities
from .. import stage


@stage.stage_class('MessageProcessor')
class Processor(stage.PipelineStage):
    """请求实际处理阶段

    通过命令处理器和聊天处理器处理消息。

    改写：
        - resp_messages
    """

    cmd_handler: handler.MessageHandler

    chat_handler: handler.MessageHandler

    async def initialize(self, pipeline_config: dict):
        self.cmd_handler = command.CommandHandler(self.ap)
        self.chat_handler = chat.ChatMessageHandler(self.ap)

        await self.cmd_handler.initialize()
        await self.chat_handler.initialize()

    async def process(
        self,
        query: core_entities.Query,
        stage_inst_name: str,
    ) -> entities.StageProcessResult:
        """处理"""
        message_text = str(query.message_chain).strip()

        self.ap.logger.info(
            f'处理 {query.launcher_type.value}_{query.launcher_id} 的请求({query.query_id}): {self._prepare_query_for_logging(query.message_chain)}'
        )

        async def generator():
            cmd_prefix = self.ap.instance_config.data['command']['prefix']

            if any(message_text.startswith(prefix) for prefix in cmd_prefix):
                async for result in self.cmd_handler.handle(query):
                    yield result
            else:
                async for result in self.chat_handler.handle(query):
                    yield result

        return generator()

    def _prepare_query_for_logging(self, data):
        """准备用于日志打印的数据，递归地截断长字段，避免序列化问题"""
        
        def _truncate_recursive(item):
            if isinstance(item, dict):
                new_dict = {}
                for k, v in item.items():
                    try:
                        # 尝试序列化，如果失败则跳过
                        copy.deepcopy(v)
                        if 'base64' in k and isinstance(v, str):
                            new_dict[k] = v[:20] + '...' if len(v) > 20 else v
                        else:
                            new_dict[k] = _truncate_recursive(v)
                    except (TypeError, pickle.PickleError):
                        new_dict[k] = f"<{type(v).__name__} object is not serializable>"
                return new_dict
            elif isinstance(item, list):
                return [_truncate_recursive(elem) for elem in item]
            elif hasattr(item, '__dict__'):
                # 对于对象，只处理它的 __dict__
                return _truncate_recursive(vars(item))
            else:
                return item

        # 不再使用 deepcopy(data)
        return _truncate_recursive(data)