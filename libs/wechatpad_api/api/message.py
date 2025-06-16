from typing import Dict, List, Optional
from libs.wechatpad_api.util.http_util import async_request, post_json, get_json


class MessageApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化MessageApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def send_text_message(self, key: str, to_user_name: str, content: str, at_wxid_list: Optional[List[str]] = None) -> Dict:
        """
        发送文本消息
        Args:
            key: 账号唯一标识
            to_user_name: 接收者wxid
            content: 文本类型消息时内容
            at_wxid_list: 发送艾特消息时的 wxid 列表 (可选)
        Returns:
            Dict: 发送消息操作的结果
        """
        url = f"{self.base_url}/message/SendTextMessage"
        msg_item = {
            "AtWxIDList": at_wxid_list if at_wxid_list is not None else [],
            "ImageContent": "",
            "MsgType": 1,  # 1 Text
            "TextContent": content,
            "ToUserName": to_user_name
        }
        json_data = {"MsgItem": [msg_item]}
        return post_json(base_url=url, token=key, data=json_data)

    def send_image_message(self, key: str, to_user_name: str, image_content: str, at_wxid_list: Optional[List[str]] = None) -> Dict:
        """
        发送图片消息
        Args:
            key: 账号唯一标识
            to_user_name: 接收者wxid
            image_content: 图片类型消息时图片的 base64 编码
            at_wxid_list: 发送艾特消息时的 wxid 列表 (可选)
        Returns:
            Dict: 发送图片消息操作的结果
        """
        url = f"{self.base_url}/message/SendImageMessage"
        msg_item = {
            "AtWxIDList": at_wxid_list if at_wxid_list is not None else [],
            "ImageContent": image_content,
            "MsgType": 2,  # 2 Image
            "TextContent": "",
            "ToUserName": to_user_name
        }
        json_data = {"MsgItem": [msg_item]}
        return post_json(base_url=url, token=key, data=json_data)

    def send_voice(self, key: str, to_user_name: str, voice_data: str, voice_format: int, voice_second: int) -> Dict:
        """
        发送语音
        Args:
            key: 账号唯一标识
            to_user_name: 接收者wxid
            voice_data: 语音数据 (Base64编码)
            voice_format: 语音格式
            voice_second: 语音时长 (秒)
        Returns:
            Dict: 发送语音操作的结果
        """
        url = f"{self.base_url}/message/SendVoice"
        json_data = {
            "ToUserName": to_user_name,
            "VoiceData": voice_data,
            "VoiceFormat": voice_format,
            "VoiceSecond": voice_second
        }
        return post_json(base_url=url, token=key, data=json_data)

    def share_card_message(self, key: str, to_user_name: str, card_wx_id: str, card_nick_name: str, card_flag: int, card_alias: str = "") -> Dict:
        """
        分享名片消息
        Args:
            key: 账号唯一标识
            to_user_name: 消息接收者
            card_wx_id: 名片wxid
            card_nick_name: 名片昵称
            card_flag: 名片CertFlag (0:个人名片 24:公众号名片)
            card_alias: 名片别名(发送公众号名片时留空)
        Returns:
            Dict: 分享名片消息操作的结果
        """
        url = f"{self.base_url}/message/ShareCardMessage"
        param = {
            "CardAlias": card_alias,
            "CardFlag": card_flag,
            "CardNickName": card_nick_name,
            "CardWxId": card_wx_id,
            "ToUserName": to_user_name
        }
        return post_json(base_url=url, token=key, data=param)

    def send_emoji_message(self, key: str, emoji_list: List[Dict]) -> Dict:
        """
        发送表情
        Args:
            key: 账号唯一标识
            emoji_list: 表情列表，每个元素为包含 "EmojiMd5", "EmojiSize", "ToWxid" 的字典
        Returns:
            Dict: 发送表情操作的结果
        """
        url = f"{self.base_url}/message/SendEmojiMessage"
        json_data = {"EmojiList": emoji_list}
        return post_json(base_url=url, token=key, data=json_data)

    def send_app_message(self, key: str, app_list: List[Dict]) -> Dict:
        """
        发送App消息
        Args:
            key: 账号唯一标识
            app_list: App消息列表，每个元素为包含 "ContentType", "ContentXML", "ToWxid" 的字典
        Returns:
            Dict: 发送App消息操作的结果
        """
        url = f"{self.base_url}/message/SendAppMessage"
        json_data = {"AppList": app_list}
        return post_json(base_url=url, token=key, data=json_data)

    def revoke_msg(self, key: str, to_user_name: str, client_msg_id: int, create_time: int, new_msg_id: str) -> Dict:
        """
        撤销消息
        Args:
            key: 账号唯一标识
            to_user_name: 接收者wxid
            client_msg_id: 客户端消息ID
            create_time: 创建时间
            new_msg_id: 新消息ID
        Returns:
            Dict: 撤销消息操作的结果
        """
        param = {
            "ClientMsgId": client_msg_id,
            "CreateTime": create_time,
            "NewMsgId": new_msg_id,
            "ToUserName": to_user_name
        }
        url = f"{self.base_url}/message/RevokeMsg"
        return post_json(base_url=url, token=key, data=param)
        
    def add_message_mgr(self, key: str, msg_item: List[Dict]) -> Dict:
        """
        添加要发送的文本消息进入管理器
        Args:
            key: 账号唯一标识
            msg_item: 消息体数组，格式同SendMessageModel
        Returns:
            Dict: 添加消息到管理器操作的结果
        """
        url = f"{self.base_url}/message/AddMessageMgr"
        json_data = {"MsgItem": msg_item}
        return post_json(base_url=url, token=key, data=json_data)
        
    def cdn_upload_video(self, key: str, thumb_data: str, to_user_name: str, video_data: List[int]) -> Dict:
        """
        上传视频
        Args:
            key: 账号唯一标识
            thumb_data: ThumbData (Base64编码)
            to_user_name: ToWxid
            video_data: 视频数据 (字节数组)
        Returns:
            Dict: 上传视频操作的结果
        """
        url = f"{self.base_url}/message/CdnUploadVideo"
        json_data = {
            "ThumbData": thumb_data,
            "ToUserName": to_user_name,
            "VideoData": video_data
        }
        return post_json(base_url=url, token=key, data=json_data)
        
    def forward_emoji(self, key: str, emoji_list: List[Dict]) -> Dict:
        """
        转发表情，包含动图
        Args:
            key: 账号唯一标识
            emoji_list: 表情列表，每个元素为包含 "EmojiMd5", "EmojiSize", "ToWxid" 的字典
        Returns:
            Dict: 转发表情操作的结果
        """
        url = f"{self.base_url}/message/ForwardEmoji"
        json_data = {"EmojiList": emoji_list}
        return post_json(base_url=url, token=key, data=json_data)
        
    def forward_image_message(self, key: str, forward_image_list: List[Dict]) -> Dict:
        """
        转发图片
        Args:
            key: 账号唯一标识
            forward_image_list: 图片列表，每个元素为包含 "AesKey", "CdnMidImgSize", "CdnMidImgUrl", "CdnThumbImgSize", "ToUserName" 的字典
        Returns:
            Dict: 转发图片操作的结果
        """
        url = f"{self.base_url}/message/ForwardImageMessage"
        json_data = {"ForwardImageList": forward_image_list}
        return post_json(base_url=url, token=key, data=json_data)
        
    def forward_video_message(self, key: str, forward_video_list: List[Dict]) -> Dict:
        """
        转发视频
        Args:
            key: 账号唯一标识
            forward_video_list: 视频列表，每个元素为包含 "AesKey", "CdnThumbLength", "CdnVideoUrl", "Length", "PlayLength", "ToUserName" 的字典
        Returns:
            Dict: 转发视频操作的结果
        """
        url = f"{self.base_url}/message/ForwardVideoMessage"
        json_data = {"ForwardVideoList": forward_video_list}
        return post_json(base_url=url, token=key, data=json_data)
        
    def get_msg_big_img(self, key: str, from_user_name: str, msg_id: int, section: Dict, to_user_name: str, total_len: int, compress_type: int = 0) -> Dict:
        """
        获取图片(高清图片下载)
        Args:
            key: 账号唯一标识
            from_user_name: 下载图片时，图片消息的发送者
            msg_id: 消息ID (注意是msg_id 不是new_msg_id)
            section: 当前要获取的数据分包 {"DataLen": 数据分包长度, "StartPos": 数据分包开始位置}
            to_user_name: 下载图片时，图片消息的接收者
            total_len: 下载数据的总长度
            compress_type: 下载图片时，数据压缩类型(默认为0即可)
        Returns:
            Dict: 高清图片下载结果
        """
        url = f"{self.base_url}/message/GetMsgBigImg"
        json_data = {
            "CompressType": compress_type,
            "FromUserName": from_user_name,
            "MsgId": msg_id,
            "Section": section,
            "ToUserName": to_user_name,
            "TotalLen": total_len
        }
        return post_json(base_url=url, token=key, data=json_data)
        
    def get_msg_video(self, key: str, from_user_name: str, msg_id: int, section: Dict, to_user_name: str, total_len: int) -> Dict:
        """
        获取视频(视频数据下载)
        Args:
            key: 账号唯一标识
            from_user_name: 下载视频时，视频消息的发送者
            msg_id: 消息ID (注意是msg_id 不是new_msg_id)
            section: 当前要获取的数据分包 {"DataLen": 数据分包长度, "StartPos": 数据分包开始位置}
            to_user_name: 下载视频时，视频消息的接收者
            total_len: 下载数据的总长度
        Returns:
            Dict: 视频数据下载结果
        """
        url = f"{self.base_url}/message/GetMsgVideo"
        json_data = {
            "FromUserName": from_user_name,
            "MsgId": msg_id,
            "Section": section,
            "ToUserName": to_user_name,
            "TotalLen": total_len
        }
        return post_json(base_url=url, token=key, data=json_data)
        
    def get_msg_voice(self, key: str, bufid: str, length: int, new_msg_id: str, to_user_name: str) -> Dict:
        """
        下载语音消息
        Args:
            key: 账号唯一标识
            bufid: Bufid
            length: Length
            new_msg_id: NewMsgId
            to_user_name: ToWxid
        Returns:
            Dict: 语音消息下载结果
        """
        url = f"{self.base_url}/message/GetMsgVoice"
        json_data = {
            "Bufid": bufid,
            "Length": length,
            "NewMsgId": new_msg_id,
            "ToUserName": to_user_name
        }
        return post_json(base_url=url, token=key, data=json_data)
        
    def group_mass_msg_image(self, key: str, image_base64: str, to_user_name: List[str]) -> Dict:
        """
        群发图片
        Args:
            key: 账号唯一标识
            image_base64: 图片Base64编码
            to_user_name: 接收者wxid列表
        Returns:
            Dict: 群发图片操作的结果
        """
        url = f"{self.base_url}/message/GroupMassMsgImage"
        json_data = {
            "ImageBase64": image_base64,
            "ToUserName": to_user_name
        }
        return post_json(base_url=url, token=key, data=json_data)
        
    def group_mass_msg_text(self, key: str, content: str, to_user_name: List[str]) -> Dict:
        """
        群发接口 (群发文本消息)
        Args:
            key: 账号唯一标识
            content: 消息内容
            to_user_name: 接收者wxid列表
        Returns:
            Dict: 群发文本消息操作的结果
        """
        url = f"{self.base_url}/message/GroupMassMsgText"
        json_data = {
            "Content": content,
            "ToUserName": to_user_name
        }
        return post_json(base_url=url, token=key, data=json_data)
        
    def http_sync_msg(self, key: str, count: int = 0) -> Dict:
        """
        同步消息, HTTP-轮询方式
        Args:
            key: 账号唯一标识
            count: 同步几条消息; 接收空请求体, 默认为0, 同步所有消息
        Returns:
            Dict: 同步消息操作的结果
        """
        url = f"{self.base_url}/message/HttpSyncMsg"
        json_data = {"Count": count}
        return post_json(base_url=url, token=key, data=json_data)
        
    def new_sync_history_message(self, key: str) -> Dict:
        """
        同步历史消息
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 同步历史消息操作的结果
        """
        url = f"{self.base_url}/message/NewSyncHistoryMessage"
        return post_json(base_url=url, token=key)
        
    def revoke_msg_new(self, key: str, client_msg_id: int, create_time: int, new_msg_id: str, to_user_name: str) -> Dict:
        """
        撤回消息（New）
        Args:
            key: 账号唯一标识
            client_msg_id: 客户端消息ID
            create_time: 创建时间
            new_msg_id: 新消息ID
            to_user_name: 接收者wxid
        Returns:
            Dict: 撤回消息操作的结果
        """
        param = {
            "ClientMsgId": client_msg_id,
            "CreateTime": create_time,
            "NewMsgId": new_msg_id,
            "ToUserName": to_user_name
        }
        url = f"{self.base_url}/message/RevokeMsgNew"
        return post_json(base_url=url, token=key, data=param)

    def send_cdn_download(self, key: str, aeskey: str, file_type: int, file_url: str) -> Dict:
        """
        下载 请求
        Args:
            key: 账号唯一标识
            aeskey: AesKey
            file_type: 文件类型
            file_url: 文件URL
        Returns:
            Dict: 下载请求操作的结果
        """
        url = f"{self.base_url}/message/SendCdnDownload"
        json_data = {
            "AesKey": aeskey,
            "FileType": file_type,
            "FileUrl": file_url
        }
        return post_json(base_url=url, token=key, data=json_data)