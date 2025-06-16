from typing import Dict, List, Any, Optional
from libs.wechatpad_api.util.http_util import post_json, get_json

class FavorApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化FavorApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def batch_del_fav_item(self, key: str, fav_id: int, key_buf: str) -> Dict:
        """
        批量删除收藏
        Args:
            key: 账号唯一标识
            fav_id: 收藏ID
            key_buf: 解密密钥
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/favor/BatchDelFavItem"
        json_data = {"FavId": fav_id, "KeyBuf": key_buf}
        return post_json(base_url=url, token=key, data=json_data)

    def fav_sync(self, key: str) -> Dict:
        """
        同步收藏
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 收藏同步结果
        """
        url = f"{self.base_url}/favor/FavSync"
        return get_json(base_url=url, token=key)

    def get_fav_item_id(self, key: str, fav_id: int) -> Dict:
        """
        获取收藏详细
        Args:
            key: 账号唯一标识
            fav_id: 收藏ID
        Returns:
            Dict: 收藏详细信息
        """
        url = f"{self.base_url}/favor/GetFavItemId"
        json_data = {"FavId": fav_id}
        return post_json(base_url=url, token=key, data=json_data)

    def get_fav_list(self, key: str, fav_id: int = 0, key_buf: str = "") -> Dict:
        """
        获取收藏list
        Args:
            key: 账号唯一标识
            fav_id: 收藏ID (可选，用于分页或特定查询)
            key_buf: KeyBuf (可选，用于分页或特定查询)
        Returns:
            Dict: 收藏列表信息
        """
        url = f"{self.base_url}/favor/GetFavList"
        json_data = {
            "FavId": fav_id,
            "KeyBuf": key_buf
        }
        return post_json(base_url=url, token=key, data=json_data)