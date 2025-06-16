from typing import Dict, List, Optional
from libs.wechatpad_api.util.http_util import async_request, post_json, get_json

"""
微信标签管理API接口
包含所有/label/路径下的微信标签管理功能
"""
class LabelApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化LabelApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def add_contact_label(self, key: str, label_id: str, label_name_list: List[str]) -> Dict:
        """
        添加列表
        Args:
            key: 账号唯一标识
            label_id: 标签ID
            label_name_list: 标签名称列表
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/label/AddContactLabel"
        json_data = {
            "LabelId": label_id,
            "LabelNameList": label_name_list
        }
        return post_json(base_url=url, token=key, data=json_data)
 
    def del_contact_label(self, key: str, label_id: str) -> Dict:
        """
        删除标签
        Args:
            key: 账号唯一标识
            label_id: 要删除的标签ID
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/label/DelContactLabel"
        json_data = {"LabelId": label_id}
        return post_json(base_url=url, token=key, data=json_data)
 
    def get_contact_label_list(self, key: str) -> Dict:
        """
        获取标签列表
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 标签列表信息
        """
        url = f"{self.base_url}/label/GetContactLabelList"
        return get_json(base_url=url, token=key)
 
    def modify_label(self, key: str, label_id: str, label_name_list: List[str]) -> Dict:
        """
        修改标签
        Args:
            key: 账号唯一标识
            label_id: 要修改的标签ID
            label_name_list: 新的标签名称列表
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/label/ModifyLabel"
        json_data = {
            "LabelId": label_id,
            "LabelNameList": label_name_list
        }
        return post_json(base_url=url, token=key, data=json_data)
 
    def get_wx_friend_list_by_label(self, key: str, label_id: str) -> Dict:
        """
        获取标签下所有好友
        Args:
            key: 账号唯一标识
            label_id: 标签ID
        Returns:
            Dict: 标签下的好友列表
        """
        url = f"{self.base_url}/label/GetWXFriendListByLabel"
        json_data = {"LabelId": label_id}
        return post_json(base_url=url, token=key, data=json_data)