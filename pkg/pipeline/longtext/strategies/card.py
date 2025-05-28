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
        # Send to render API
        render_url = "http://192.168.110.254:8123/mra/render"
        async with aiohttp.ClientSession() as session:
            async with session.post(render_url, json={"markdown": message}) as resp:
                if resp.status == 200:
                    result_json = await resp.json()
                    result_url = result_json['url']
                    # Replace localhost if needed
                    result_url = result_url.replace('http://localhost:8080', 'https://sp.jiudingsupply.com')
                    
                    thumb_url = await self.get_dynamic_thumb_url()
                else:
                    error = await resp.text()
                    self.ap.logger.error(f"Render API error: {error}")
                    # 先过滤掉<think>...</think>标签中的内容
                    think_pattern = r'<think>.*?</think>'
                    clean_text = re.sub(think_pattern, '', message, flags=re.DOTALL)
                    return [platform_message.Plain(text=clean_text)]

        app_msg = f'''
<appmsg sdkver="1">
    <title>点击一下你就知道</title>
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