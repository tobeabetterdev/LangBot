# 卡片式消息组件
from __future__ import annotations
import re

import aiohttp

from .. import strategy as strategy_model
from ....core import entities as core_entities
from ....platform.types import message as platform_message


WeChatAppMsg = platform_message.WeChatAppMsg


@strategy_model.strategy_class('card')
class CardComponentStrategy(strategy_model.LongTextStrategy):

    async def process(self, message: str, query: core_entities.Query) -> list[platform_message.MessageComponent]:
        # 获取message_id
        message_id = query.variables.get('answer_message_id', '')
        if not message_id:
            # 没有message_id时直接返回清理后的纯文本
            clean_text = await self._clean_message(message)
            return [platform_message.Plain(text=clean_text)]
        
        # 调用渲染API
        render_url = f"https://sp.jiudingsupply.com/mra/messages/{message_id}"
        thumb_url = 'https://api.pearktrue.cn/api/animal/'

        # 获取发送者昵称
        sender_nickname = "用户"
        if query.message_event and hasattr(query.message_event, 'source_platform_object'):
            source_obj = query.message_event.source_platform_object
            if 'sender_nickname' in source_obj:
                sender_nickname = source_obj['sender_nickname']
            elif 'push_content' in source_obj:
                push_content = source_obj['push_content']
                if '在群聊中@了你' in push_content:
                    sender_nickname = push_content.split('在群聊中@了你')[0]

        # 构建微信卡片消息
        app_msg = f'''
<appmsg sdkver="1">
    <title>@{sender_nickname}</title>
    <des>{query.user_message.content[0].text}</des>
    <url>{render_url}</url>
    <thumburl>{thumb_url}</thumburl>
    <type>5</type>
    <sourceusername>wxid_una7mdzddc8y22</sourceusername>
    <sourcedisplayname>柯蓝の大脑壳</sourcedisplayname>
</appmsg>
'''
        return [
            WeChatAppMsg(app_msg=app_msg)
        ]
    
    async def _clean_message(self, message: str) -> str:
        """清理消息中的思考标签"""
        think_pattern = r'<think>.*?</think>|<detail>.*?</detail>'
        return re.sub(think_pattern, '', message, flags=re.DOTALL)
