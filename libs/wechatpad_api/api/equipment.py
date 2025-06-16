from typing import Dict, Optional
from libs.wechatpad_api.util.http_util import get_json, post_json


class EquipmentApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化EquipmentApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def get_bound_hard_device(self, key: str) -> Dict:
        """
        获取硬件设备情况
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 硬件设备信息
        """
        url = f"{self.base_url}/equipment/GetBoundHardDevice"
        return get_json(base_url=url, token=key)

    def get_online_info(self, key: str) -> Dict:
        """
        获取在线设备信息
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 在线设备信息
        """
        url = f"{self.base_url}/equipment/GetOnlineInfo"
        return get_json(base_url=url, token=key)

    def get_safety_info(self, key: str) -> Dict:
        """
        获取安全设备列表
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 安全设备信息
        """
        url = f"{self.base_url}/equipment/GetSafetyInfo"
        return post_json(base_url=url, token=key)

    def del_safe_device(self, key: str, device_uuid: str) -> Dict:
        """
        删除安全设备
        Args:
            key: 账号唯一标识
            device_uuid: 要删除的设备UUID
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/equipment/DelSafeDevice"
        json_data = {"DeviceUUID": device_uuid}
        return post_json(base_url=url, token=key, data=json_data)