from typing import Dict, Optional
from libs.wechatpad_api.util.http_util import post_json

class FinderApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化FinderApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def finder_follow(self, key: str, finder_user_name: str, op_type: int, poster_user_name: str = "",
                      ref_object_id: str = "", userver: int = 0, cook: str = "") -> Dict:
        """
        关注/取消视频号
        Args:
            key: 账号唯一标识
            finder_user_name: 视频号用户名
            op_type: 操作类型(1:关注 2:取消)
            poster_user_name: 发布者用户名
            ref_object_id: 参考对象ID
            userver: 用户版本号
            cook: 会话cookie
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/finder/FinderFollow"
        json_data = {
            "FinderUserName": finder_user_name,
            "OpType": op_type,
            "PosterUsername": poster_user_name,
            "RefObjectId": ref_object_id,
            "Userver": userver,
            "Cook": cook
        }
        return post_json(base_url=url, token=key, data=json_data)

    def finder_search(self, key: str, user_key: str, index: int = 0, userver: int = 0, uuid: str = "") -> Dict:
        """
        视频号搜索
        Args:
            key: 账号唯一标识
            user_key: 搜索关键词
            index: 分页索引
            userver: 用户版本号
            uuid: 会话UUID
        Returns:
            Dict: 搜索结果
        """
        url = f"{self.base_url}/finder/FinderSearch"
        json_data = {
            "UserKey": user_key,
            "Index": index,
            "Userver": userver,
            "Uuid": uuid
        }
        return post_json(base_url=url, token=key, data=json_data)

    def finder_user_prepare(self, key: str, userver: int = 0) -> Dict:
        """
        视频号中心准备
        Args:
            key: 账号唯一标识
            userver: 用户版本号
        Returns:
            Dict: 准备结果
        """
        url = f"{self.base_url}/finder/FinderUserPrepare"
        json_data = {"Userver": userver}
        return post_json(base_url=url, token=key, data=json_data)