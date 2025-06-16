from typing import Dict, List, Optional
from libs.wechatpad_api.util.http_util import post_json, get_json


class SnsApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化SnsApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def download_media(self, key: str, url: str) -> Dict:
        """
        下载朋友圈视频
        Args:
            key: 账号唯一标识
            url: 视频URL
        Returns:
            Dict: 下载朋友圈视频操作的结果
        """
        api_url = f"{self.base_url}/sns/DownloadMedia"
        json_data = {
            "URL": url
        }
        return post_json(base_url=api_url, token=key, data=json_data)

    def get_collect_circle(self, key: str, black_list: Optional[List[str]] = None, fav_item_id: int = 0, location: Optional[Dict] = None, location_val: int = 0, source_id: str = "") -> Dict:
        """
        获取收藏朋友圈详情
        Args:
            key: 账号唯一标识
            black_list: 不可见好友列表
            fav_item_id: 收藏项ID
            location: 位置信息
            location_val: 位置值
            source_id: 来源ID
        Returns:
            Dict: 收藏朋友圈详情
        """
        url = f"{self.base_url}/sns/GetCollectCircle"
        json_data = {
            "BlackList": black_list if black_list is not None else [],
            "FavItemID": fav_item_id,
            "Location": location,
            "LocationVal": location_val,
            "SourceID": source_id
        }
        return post_json(base_url=url, token=key, data=json_data)

    def get_sns_sync(self, key: str) -> Dict:
        """
        同步朋友圈
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 朋友圈同步结果
        """
        url = f"{self.base_url}/sns/GetSnsSync"
        return post_json(base_url=url, token=key)

    def send_cdn_sns_video_upload_request(self, key: str) -> Dict:
        """
        上传朋友圈视频
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 上传朋友圈视频操作的结果
        """
        url = f"{self.base_url}/sns/SendCdnSnsVideoUploadReuqest"
        return post_json(base_url=url, token=key)

    def send_fav_item_circle(self, key: str, black_list: Optional[List[str]] = None, fav_item_id: int = 0, location: Optional[Dict] = None, location_val: int = 0, source_id: str = "") -> Dict:
        """
        转发收藏朋友圈
        Args:
            key: 账号唯一标识
            black_list: 不可见好友列表
            fav_item_id: 收藏项ID
            location: 位置信息
            location_val: 位置值
            source_id: 来源ID
        Returns:
            Dict: 转发收藏朋友圈操作的结果
        """
        url = f"{self.base_url}/sns/SendFavItemCircle"
        json_data = {
            "BlackList": black_list if black_list is not None else [],
            "FavItemID": fav_item_id,
            "Location": location,
            "LocationVal": location_val,
            "SourceID": source_id
        }
        return post_json(base_url=url, token=key, data=json_data)

    def send_friend_circle(self, key: str, content: str = "", content_style: int = 0, content_url: str = "", description: str = "",
                            group_user_list: Optional[List[str]] = None, image_data_list: Optional[List[str]] = None,
                            location_info: Optional[Dict] = None, media_list: Optional[List[Dict]] = None,
                            privacy: int = 0, video_data_list: Optional[List[str]] = None, with_user_list: Optional[List[str]] = None) -> Dict:
        """
        发送朋友圈
        Args:
            key: 账号唯一标识
            content: 文本内容
            content_style: 纯文字/图文/引用/视频
            content_url: 内容URL
            description: 描述
            group_user_list: 可见好友列表
            image_data_list: 图片数据列表 (Base64编码)
            location_info: 发送朋友圈的位置信息
            media_list: 图片/视频列表
            privacy: 是否仅自己可见
            video_data_list: 视频数据列表 (Base64编码)
            with_user_list: 提醒好友看列表
        Returns:
            Dict: 发送朋友圈操作的结果
        """
        url = f"{self.base_url}/sns/SendFriendCircle"
        json_data = {
            "Content": content,
            "ContentStyle": content_style,
            "ContentUrl": content_url,
            "Description": description,
            "GroupUserList": group_user_list if group_user_list is not None else [],
            "ImageDataList": image_data_list if image_data_list is not None else [],
            "LocationInfo": location_info,
            "MediaList": media_list if media_list is not None else [],
            "Privacy": privacy,
            "VideoDataList": video_data_list if video_data_list is not None else [],
            "WithUserList": with_user_list if with_user_list is not None else []
        }
        return post_json(base_url=url, token=key, data=json_data)

    def send_friend_circle_by_xml(self, key: str, action_info: Optional[Dict] = None, app_info: Optional[Dict] = None, content_desc: str = "",
                                  content_desc_scene: int = 0, content_desc_show_type: int = 0, content_object: Optional[Dict] = None,
                                  create_time: int = 0, _id: int = 0, location: Optional[Dict] = None, _private: int = 0,
                                  public_user_name: str = "", show_flag: int = 0, sight_folded: int = 0,
                                  source_nick_name: str = "", source_user_name: str = "", stat_ext_str: str = "",
                                  statistics_data: str = "", stream_video: Optional[Dict] = None, user_name: str = "") -> Dict:
        """
        发送朋友圈XML结构
        Args:
            key: 账号唯一标识
            action_info: ActionInfo
            app_info: AppInfo
            content_desc: 内容描述
            content_desc_scene: 内容描述场景
            content_desc_show_type: 内容描述显示类型
            content_object: ContentObject
            create_time: 创建时间
            _id: ID
            location: 位置信息
            _private: 隐私设置
            public_user_name: 公众号用户名
            show_flag: 显示标志
            sight_folded: 视频折叠
            source_nick_name: 来源昵称
            source_user_name: 来源用户名
            stat_ext_str: 统计扩展字符串
            statistics_data: 统计数据
            stream_video: StreamVideo
            user_name: 用户名
        Returns:
            Dict: 发送朋友圈XML结构操作的结果
        """
        url = f"{self.base_url}/sns/SendFriendCircleByXMl"
        json_data = {
            "ActionInfo": action_info,
            "AppInfo": app_info,
            "ContentDesc": content_desc,
            "ContentDescScene": content_desc_scene,
            "ContentDescShowType": content_desc_show_type,
            "ContentObject": content_object,
            "CreateTime": create_time,
            "ID": _id,
            "Location": location,
            "Private": _private,
            "PublicUserName": public_user_name,
            "ShowFlag": show_flag,
            "SightFolded": sight_folded,
            "SourceNickName": source_nick_name,
            "SourceUserName": source_user_name,
            "StatExtStr": stat_ext_str,
            "StatisticsData": statistics_data,
            "StreamVideo": stream_video,
            "UserName": user_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def send_one_id_circle(self, key: str, black_list: Optional[List[str]] = None, id: str = "", location: Optional[Dict] = None, location_val: int = 0) -> Dict:
        """
        一键转发朋友圈
        Args:
            key: 账号唯一标识
            black_list: 黑名单
            id: ID
            location: 位置信息
            location_val: 位置值
        Returns:
            Dict: 一键转发朋友圈操作的结果
        """
        url = f"{self.base_url}/sns/SendOneIdCircle"
        json_data = {
            "BlackList": black_list if black_list is not None else [],
            "Id": id,
            "Location": location,
            "LocationVal": location_val
        }
        return post_json(base_url=url, token=key, data=json_data)

    def send_sns_comment(self, key: str, sns_comment_list: List[Dict], tx: bool) -> Dict:
        """
        点赞评论
        Args:
            key: 账号唯一标识
            sns_comment_list: 朋友圈评论列表，每个元素为包含 "Content", "CreateTime", "ItemID", "OpType", "ReplyCommentID", "ReplyItem", "ToUserName" 的字典
            tx: Tx
        Returns:
            Dict: 点赞评论操作的结果
        """
        url = f"{self.base_url}/sns/SendSnsComment"
        json_data = {
            "SnsCommentList": sns_comment_list,
            "Tx": tx
        }
        return post_json(base_url=url, token=key, data=json_data)

    def send_sns_object_detail_by_id(self, key: str, black_list: Optional[List[str]] = None, id: str = "", location: Optional[Dict] = None, location_val: int = 0) -> Dict:
        """
        获取指定id朋友圈
        Args:
            key: 账号唯一标识
            black_list: 黑名单
            id: ID
            location: 位置信息
            location_val: 位置值
        Returns:
            Dict: 指定id朋友圈详情
        """
        url = f"{self.base_url}/sns/SendSnsObjectDetailById"
        json_data = {
            "BlackList": black_list if black_list is not None else [],
            "Id": id,
            "Location": location,
            "LocationVal": location_val
        }
        return post_json(base_url=url, token=key, data=json_data)

    def send_sns_object_op(self, key: str, sns_object_op_list: List[Dict]) -> Dict:
        """
        朋友圈操作
        Args:
            key: 账号唯一标识
            sns_object_op_list: 朋友圈操作列表，每个元素为包含 "Data", "DataLen", "Ext", "OpType", "SnsObjID" 的字典
        Returns:
            Dict: 朋友圈操作的结果
        """
        url = f"{self.base_url}/sns/SendSnsObjectOp"
        json_data = {"SnsObjectOpList": sns_object_op_list}
        return post_json(base_url=url, token=key, data=json_data)

    def send_sns_time_line(self, key: str, first_page_md5: str = "", max_id: int = 0, user_name: str = "") -> Dict:
        """
        获取朋友圈主页
        Args:
            key: 账号唯一标识
            first_page_md5: 第一页MD5
            max_id: 最大ID
            user_name: 用户名
        Returns:
            Dict: 朋友圈主页信息
        """
        url = f"{self.base_url}/sns/SendSnsTimeLine"
        json_data = {
            "FirstPageMD5": first_page_md5,
            "MaxID": max_id,
            "UserName": user_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def send_sns_user_page(self, key: str, first_page_md5: str = "", max_id: int = 0, user_name: str = "") -> Dict:
        """
        获取指定人朋友圈
        Args:
            key: 账号唯一标识
            first_page_md5: 第一页MD5
            max_id: 最大ID
            user_name: 用户名
        Returns:
            Dict: 指定人朋友圈信息
        """
        url = f"{self.base_url}/sns/SendSnsUserPage"
        json_data = {
            "FirstPageMD5": first_page_md5,
            "MaxID": max_id,
            "UserName": user_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def set_background_image(self, key: str, url: str) -> Dict:
        """
        设置朋友圈背景图片
        Args:
            key: 账号唯一标识
            url: 背景图片URL
        Returns:
            Dict: 设置朋友圈背景图片操作的结果
        """
        api_url = f"{self.base_url}/sns/SetBackgroundImage"
        json_data = {"Url": url}
        return post_json(base_url=api_url, token=key, data=json_data)

    def set_friend_circle_days(self, key: str, function: int, value: int) -> Dict:
        """
        设置朋友圈可见天数
        Args:
            key: 账号唯一标识
            function: 功能
            value: 值
        Returns:
            Dict: 设置朋友圈可见天数操作的结果
        """
        url = f"{self.base_url}/sns/SetFriendCircleDays"
        json_data = {
            "Function": function,
            "Value": value
        }
        return post_json(base_url=url, token=key, data=json_data)

    def upload_friend_circle_image(self, key: str, image_data_list: Optional[List[str]] = None, video_data_list: Optional[List[str]] = None) -> Dict:
        """
        上传图片信息 (朋友圈)
        Args:
            key: 账号唯一标识
            image_data_list: 图片数据列表 (Base64编码)
            video_data_list: 视频数据列表 (Base64编码)
        Returns:
            Dict: 上传图片信息操作的结果
        """
        url = f"{self.base_url}/sns/UploadFriendCircleImage"
        json_data = {
            "ImageDataList": image_data_list if image_data_list is not None else [],
            "VideoDataList": video_data_list if video_data_list is not None else []
        }
        return post_json(base_url=url, token=key, data=json_data)