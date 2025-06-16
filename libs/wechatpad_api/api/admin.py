from typing import Dict
from libs.wechatpad_api.util.http_util import get_json, post_json


class AdminApi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def delay_auth_key(self, key: str, days: int = 30, expiry_date: str = None) -> Dict:
        """延期授权码
        Args:
            key: 账号唯一标识
            days: AuthKey的延期天数(默认30天)
            expiry_date: AuthKey的到期日期(例如: 2024-01-01); 与 Days 参数只能选其一(优先使用 ExpiryDate 参数)
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/admin/DelayAuthKey"
        json_data = {
            "Days": days
        }
        if expiry_date:
            json_data["ExpiryDate"] = expiry_date
        return post_json(url, token=key, data=json_data)

    def delete_auth_key(self, key: str, opt: int = 0) -> Dict:
        """删除授权码
        Args:
            key: 账号唯一标识
            opt: 删除操作类型(0:仅删除授权码 1:删除授权码相关的所有数据)
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/admin/DeleteAuthKey"
        json_data = {
            "Opt": opt
        }
        return post_json(url, token=key, data=json_data)

    def gen_auth_key1(self, key: str, count: int = 1, days: int = 365) -> Dict:
        """生成授权码(新设备)
        Args:
            key: 账号唯一标识
            count: 要生成的授权码数量(默认1)
            days: 授权码有效期天数(默认365天)
        Returns:
            Dict: 生成结果
        """
        url = f"{self.base_url}/admin/GenAuthKey1"
        json_data = {"Count": count, "Days": days}
        return post_json(url, token=key, data=json_data)
    
    def gen_auth_key2(self, key: str) -> Dict:
        """生成授权码(新设备) - GET接口
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 生成结果
        """
        url = f"{self.base_url}/admin/GenAuthKey2"
        return get_json(url, token=key)