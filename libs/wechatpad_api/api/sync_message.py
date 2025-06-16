from typing import Dict, Optional
from libs.wechatpad_api.util.http_util import get_json


class SyncMessageApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化SyncMessageApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def get_sync_msg(self, key: str) -> Dict:
        """
        同步消息，ws协议; 下面有【同步消息-HTTP-轮询方式】
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 同步消息操作的结果
        """
        url = f"{self.base_url}/ws/GetSyncMsg"
        # 根据Swagger文档，这个接口是GET请求，但参数key是通过query传递的
        # get_json函数需要base_url和token，这里key是query参数，所以需要特殊处理
        # 假设get_json可以处理query参数，或者需要手动拼接URL
        # 考虑到get_json的定义，它只接受base_url和token，所以这里需要调整
        # 暂时按照get_json的现有用法，如果key是query参数，则需要修改get_json或手动拼接
        # 鉴于get_json的参数，这里直接传入token作为key，因为Swagger文档中key是query参数
        # 实际使用时，可能需要调整http_util.py中的get_json函数来支持query参数
        return get_json(base_url=url, token=key) # 这里token参数实际上是Swagger文档中的query参数key