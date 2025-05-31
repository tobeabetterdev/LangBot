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
        render_url = f"http://192.168.110.254:8123/conversations/messages/{message_id}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(render_url, json={"markdown": message}) as resp:
                    if resp.status == 200:
                        result_json = await resp.json()
                        result_url = result_json['url']
                        # 替换localhost为生产域名
                        result_url = result_url.replace('http://localhost:8080', 'https://sp.jiudingsupply.com')
                        
                        thumb_url = await self.get_dynamic_thumb_url()
                    else:
                        error = await resp.text()
                        self.ap.logger.error(f"Render API error: {error}")
                        # API调用失败时返回清理后的纯文本
                        clean_text = await self._clean_message(message)
                        return [platform_message.Plain(text=clean_text)]
        except Exception as e:
            self.ap.logger.error(f"Render API exception: {str(e)}")
            clean_text = await self._clean_message(message)
            return [platform_message.Plain(text=clean_text)]

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
    <url>{result_url}</url>
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

    async def get_dynamic_thumb_url(self) -> str:
        """获取动态缩略图URL"""
        try:
            zoomout_url = "http://192.168.110.254:8123/mra/zoomout?url=https://api.pearktrue.cn/api/animal/"
            async with aiohttp.ClientSession() as session:
                async with session.get(zoomout_url) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        thumb_url = data.get("url", "")
                        if thumb_url:
                            # 替换localhost为生产域名
                            return thumb_url.replace('http://localhost:8080', 'https://sp.jiudingsupply.com')
        except Exception as e:
            self.ap.logger.error(f"获取动态缩略图URL失败: {e}")
        # 失败时返回默认
        return ""