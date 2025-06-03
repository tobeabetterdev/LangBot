import uuid
import aiohttp
from typing import Optional

from pkg.platform.types.message import MessageChain
from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.core import entities as core_entities
from pkg.provider.runners.difysvapi import DifyServiceAPIRunner


# 注册插件
@register(name="CommandTool", description="指令工具，根据用户指令返回内容", version="1.0", author="lock")
class CommandTool(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        self.host = host
        self.ap = host.app

    # 异步初始化
    async def initialize(self):
        pass

    async def fetch_zhihu_hotlist(self) -> Optional[str]:
        """获取知乎热榜数据"""
        api_url = "https://api.52vmy.cn/api/wl/hot?type=zhihu"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        # 提取热榜数据并组织成文本
                        hotlist = []
                        for item in data.get('data', [])[:20]:  # 取前10条
                            hotlist.append(f"{item['index']}. {item['title']} ({item['hot']})")
                        return "\n".join(hotlist)
                    else:
                        self.ap.logger.error(f"获取知乎热榜失败，状态码：{response.status}")
                        return None
        except Exception as e:
            self.ap.logger.error(f"获取知乎热榜异常：{str(e)}")
            return None

    async def fetch_baidu_hotlist(self) -> Optional[str]:
        """获取百度热榜数据"""
        api_url = "https://api.52vmy.cn/api/wl/hot?type=baidu"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        # 提取热榜数据并组织成文本
                        hotlist = []
                        for item in data.get('data', [])[:20]:  # 取前10条
                            hotlist.append(f"{item['title']} ({item['hot']})")
                        return "\n".join(hotlist)
                    else:
                        self.ap.logger.error(f"获取百度热榜失败，状态码：{response.status}")
                        return None
        except Exception as e:
            self.ap.logger.error(f"获取百度热榜异常：{str(e)}")
            return None

    async def fetch_weibo_hotlist(self) -> Optional[str]:
        """获取微博热搜数据"""
        api_url = "https://api.52vmy.cn/api/wl/hot?type=weibo"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        # 提取热榜数据并组织成文本
                        hotlist = []
                        for item in data.get('data', [])[:20]:  # 取前10条
                            hotlist.append(f"{item['title']} ({item['hot']})")
                        return "\n".join(hotlist)
                    else:
                        self.ap.logger.error(f"获取微博热搜失败，状态码：{response.status}")
                        return None
        except Exception as e:
            self.ap.logger.error(f"获取微博热搜异常：{str(e)}")
            return None

    async def call_dify_service(
        self,
        pipeline_cfg: dict,
        query: core_entities.Query
    ) -> Optional[str]:
        """调用 Dify 服务并返回响应内容"""
        try:
            # 初始化 Dify runner
            runner = DifyServiceAPIRunner(
                ap=self.ap,
                pipeline_config=pipeline_cfg['config']
            )
            
            reply_content = ""
            async for response in runner.run(query):
                if response.content:
                    content = response.content
                    if isinstance(content, list):
                        # 处理多元素内容
                        for element in content:
                            if element.type == "text":
                                reply_content += element.text
                    else:
                        reply_content += content
            
            return reply_content.strip()
            
        except Exception as e:
            self.ap.logger.error(f"调用 Dify 服务失败: {str(e)}")
            return None

    # 当收到群消息时触发
    @handler(GroupMessageReceived)
    async def group_message_received(self, ctx: EventContext):
        msg = str(ctx.event.message_chain).strip()
        launcher_id = str(ctx.event.launcher_id)
        launcher_type = str(ctx.event.launcher_type)

        # 获取黑/白名单
        pipeline_cfg = await self.ap.pipeline_service.get_pipeline('0525bcd5-3c3c-48a9-aae3-17bfc94dcbaf')
        mode = pipeline_cfg['config']['trigger']['access-control']['mode']
        sess_list = pipeline_cfg['config']['trigger']['access-control'][mode]

        found = False
        if (launcher_type== 'group' and 'group_*' in sess_list) \
            or (launcher_type == 'person' and 'person_*' in sess_list):
            found = True
        else:
            for sess in sess_list:
                if sess == f"{launcher_type}_{launcher_id}":
                    found = True
                    break
        if not found:
            self.ap.logger.info('CommandTool - 黑/白名单管制不处理')
            return
        
        # 指令映射表 (指令: (平台名称, 获取函数))
        COMMAND_MAP = {
            "/知乎": ("知乎", self.fetch_zhihu_hotlist),
            "/zhihu": ("知乎", self.fetch_zhihu_hotlist),
            "/百度": ("百度", self.fetch_baidu_hotlist),
            "/baidu": ("百度", self.fetch_baidu_hotlist),
            "/微博": ("微博", self.fetch_weibo_hotlist),
            "/weibo": ("微博", self.fetch_weibo_hotlist),
            "/知乎热榜": ("知乎", self.fetch_zhihu_hotlist)  # 兼容旧指令
        }
        
        # 处理热榜指令
        if msg in COMMAND_MAP:
            platform_name, fetch_func = COMMAND_MAP[msg]
            
            # 获取热榜数据
            hotlist = await fetch_func()
            if not hotlist:
                await self.host.send_group_message(
                    launcher_id=launcher_id,
                    message_chain=MessageChain([f"获取{platform_name}热榜失败，请稍后再试"]),
                    event=ctx.event
                )
                return
            
            # 构造优化提示词 + 热榜数据
            optimized_prompt = (
                f"请根据以下{platform_name}热榜数据，根据新闻热度优先级总结摘要内容，要尽量面面俱到，"
                f"让我对当前热点信息有一个全面的了解：\n\n{hotlist}"
            )
            
            # 构造新的 Query 对象
            query = core_entities.Query(
                session=core_entities.Session(
                    session_id=str(uuid.uuid4()),
                    launcher_id=launcher_id,
                    launcher_type=core_entities.LauncherTypes(launcher_type),
                    using_conversation=core_entities.Conversation(uuid=str(uuid.uuid4()))
                ),
                user_message=core_entities.Message(
                    role="user",
                    content=optimized_prompt
                ),
                message_event=ctx.event,
                variables={}
            )
            
            # 调用 Dify 服务
            response = await self.call_dify_service(pipeline_cfg, query)
            
            if response:
                # 回复消息
                await self.host.send_group_message(
                    launcher_id=launcher_id,
                    message_chain=MessageChain([response]),
                    event=ctx.event
                )
            else:
                await self.host.send_group_message(
                    launcher_id=launcher_id,
                    message_chain=MessageChain(["服务调用失败，请稍后再试"]),
                    event=ctx.event
                )
            return
        
        # 非热榜指令保持原有处理逻辑
        # 构造 Query 对象
        query = core_entities.Query(
            session=core_entities.Session(
                session_id='command_tool@plugin',
                launcher_id=launcher_id,
                launcher_type=core_entities.LauncherTypes(launcher_type),
                using_conversation=core_entities.Conversation(uuid=str(uuid.uuid4()))
            ),
            user_message=core_entities.Message(
                role="user",
                content=msg
            ),
            message_event=ctx.event,
            variables={}
        )

        # 调用 Dify 服务
        response = await self.call_dify_service(pipeline_cfg, query)
        
        if response:
            # 回复消息
            await self.host.send_group_message(
                launcher_id=launcher_id,
                message_chain=MessageChain([response]),
                event=ctx.event
            )
        else:
            await self.host.send_group_message(
                launcher_id=launcher_id,
                message_chain=MessageChain(["服务调用失败，请稍后再试"]),
                event=ctx.event
            )