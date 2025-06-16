from typing import Dict, Optional
from libs.wechatpad_api.util.http_util import post_json, get_json


class OtherApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化OtherApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def get_people_nearby(self, key: str, latitude: float, longitude: float) -> Dict:
        """
        查看附近的人
        Args:
            key: 账号唯一标识
            latitude: 纬度
            longitude: 经度
        Returns:
            Dict: 附近的人列表
        """
        url = f"{self.base_url}/other/GetPeopleNearby"
        json_data = {
            "Latitude": latitude,
            "Longitude": longitude
        }
        return post_json(base_url=url, token=key, data=json_data)

    def get_redis_sync_msg(self, key: str) -> Dict:
        """
        获取缓存在redis中的消息
        Args:
            key: 账号唯一标识
        Returns:
            Dict: Redis中的消息
        """
        url = f"{self.base_url}/other/GetRedisSyncMsg"
        return post_json(base_url=url, token=key)

    def get_user_rank_like_count(self, key: str, rank_id: str) -> Dict:
        """
        获取步数排行数据列表
        Args:
            key: 账号唯一标识
            rank_id: 排行榜ID
        Returns:
            Dict: 步数排行数据
        """
        url = f"{self.base_url}/other/GetUserRankLikeCount"
        json_data = {"RankId": rank_id}
        return post_json(base_url=url, token=key, data=json_data)

    def redis_memory(self, key: str) -> Dict:
        """
        内存管理
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 内存管理信息
        """
        url = f"{self.base_url}/other/RedisMemory"
        return get_json(base_url=url, token=key)

    def update_step_number(self, key: str, number: int) -> Dict:
        """
        修改步数
        Args:
            key: 账号唯一标识
            number: 步数
        Returns:
            Dict: 修改步数操作的结果
        """
        url = f"{self.base_url}/other/UpdateStepNumber"
        json_data = {"Number": number}
        return post_json(base_url=url, token=key, data=json_data)