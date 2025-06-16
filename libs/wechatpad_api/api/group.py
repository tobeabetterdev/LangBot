from typing import Dict, List, Optional
from libs.wechatpad_api.util.http_util import async_request, post_json, get_json

class GroupApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化GroupApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def get_chatroom_member_detail(self, key: str, chatroom_name: str) -> Dict:
        """
        获取群成员详细信息
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
        Returns:
            Dict: 包含群成员详细信息的字典
        """
        url = f"{self.base_url}/group/GetChatroomMemberDetail"
        json_data = {"ChatRoomName": chatroom_name}
        return post_json(base_url=url, token=key, data=json_data)
    
    def add_chat_room_members(self, key: str, chatroom_name: str, user_list: List[str]) -> Dict:
        """
        添加群成员 (邀请群成员)
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            user_list: 要添加的成员wxid列表
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/InviteChatroomMembers"
        json_data = {
            "ChatRoomName": chatroom_name,
            "UserList": user_list
        }
        return post_json(base_url=url, token=key, data=json_data)
    
    def del_chat_room_members(self, key: str, chatroom_name: str, user_list: List[str]) -> Dict:
        """
        删除群成员
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            user_list: 要删除的成员wxid列表
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/SendDelDelChatRoomMember" # 根据Swagger文档，此接口为SendDelDelChatRoomMember
        json_data = {
            "ChatRoomName": chatroom_name,
            "UserList": user_list
        }
        return post_json(base_url=url, token=key, data=json_data)
    
    def add_chatroom_admin(self, key: str, chatroom_name: str, user_list: List[str]) -> Dict:
        """
        添加群管理员
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            user_list: 要设置为管理员的成员wxid列表
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/AddChatroomAdmin"
        json_data = {
            "ChatRoomName": chatroom_name,
            "UserList": user_list
        }
        return post_json(base_url=url, token=key, data=json_data)
    
    def remove_chatroom_admin(self, key: str, chatroom_name: str, user_list: List[str]) -> Dict:
        """
        删除群管理员
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            user_list: 要移除管理员权限的成员wxid列表
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/DelChatroomAdmin"
        json_data = {
            "ChatRoomName": chatroom_name,
            "UserList": user_list
        }
        return post_json(base_url=url, token=key, data=json_data)
    
    def update_chatroom_announcement(self, key: str, chatroom_name: str, content: str) -> Dict:
        """
        设置群公告
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            content: 公告内容
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/SetChatroomAnnouncement" # 根据Swagger文档，此接口为SetChatroomAnnouncement
        json_data = {
            "ChatRoomName": chatroom_name,
            "Content": content
        }
        return post_json(base_url=url, token=key, data=json_data)
    
    def send_transfer_group_owner(self, key: str, chatroom_name: str, new_owner_user_name: str) -> Dict:
        """
        转让群
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            new_owner_user_name: 新群主的wxid
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/SendTransferGroupOwner"
        json_data = {
            "ChatRoomName": chatroom_name,
            "NewOwnerUserName": new_owner_user_name
        }
        return post_json(base_url=url, token=key, data=json_data)
    
    def set_chatroom_access_verify(self, key: str, chatroom_name: str, enable: bool) -> Dict:
        """
        设置群聊邀请开关
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            enable: 是否开启验证（True为开启，False为关闭）
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/SetChatroomAccessVerify"
        json_data = {
            "ChatRoomName": chatroom_name,
            "Enable": enable
        }
        return post_json(base_url=url, token=key, data=json_data)
    
    def get_group_list(self, key: str) -> Dict:
        """
        获取群列表
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 群列表信息
        """
        url = f"{self.base_url}/group/GroupList"
        return get_json(base_url=url, token=key)
    
    def create_chat_room(self, key: str, topic: str, user_list: List[str]) -> Dict:
        """
        创建群请求
        Args:
            key: 账号唯一标识
            topic: 群聊主题
            user_list: 初始成员wxid列表
        Returns:
            Dict: 创建结果
        """
        url = f"{self.base_url}/group/CreateChatRoom"
        json_data = {
            "TopIc": topic,
            "UserList": user_list
        }
        return post_json(base_url=url, token=key, data=json_data)
    
    def quit_chatroom(self, key: str, chatroom_name: str) -> Dict:
        """
        退出群聊
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/QuitChatroom"
        json_data = {"ChatRoomName": chatroom_name}
        return post_json(base_url=url, token=key, data=json_data)
    
    def get_chatroom_qrcode(self, key: str, chatroom_name: str) -> Dict:
        """
        获取群二维码
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
        Returns:
            Dict: 包含群二维码信息的字典
        """
        url = f"{self.base_url}/group/GetChatroomQrCode"
        json_data = {"ChatRoomName": chatroom_name}
        return post_json(base_url=url, token=key, data=json_data)
    
    def set_chatroom_name(self, key: str, chatroom_name: str, nickname: str) -> Dict:
        """
        设置群昵称
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            nickname: 新的群昵称
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/SetChatroomName"
        json_data = {
            "ChatRoomName": chatroom_name,
            "Nickname": nickname
        }
        return post_json(base_url=url, token=key, data=json_data)

    def move_to_contract(self, key: str, chatroom_name: str, val: int) -> Dict:
        """
        获取群聊（MoveToContract）
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            val: 未知参数，根据接口文档为uint32类型
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/MoveToContract"
        json_data = {
            "ChatRoomName": chatroom_name,
            "Val": val
        }
        return post_json(base_url=url, token=key, data=json_data)

    def get_chatroom_announcement(self, key: str, chatroom_name: str) -> Dict:
        """
        获取群公告
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
        Returns:
            Dict: 群公告内容
        """
        url = f"{self.base_url}/group/SetGetChatRoomInfoDetail"
        json_data = {"ChatRoomName": chatroom_name}
        return post_json(base_url=url, token=key, data=json_data)

    def get_chatroom_info(self, key: str, chatroom_wxid_list: List[str]) -> Dict:
        """
        获取群详情
        Args:
            key: 账号唯一标识
            chatroom_wxid_list: 群聊ID列表（格式：["xxx@chatroom", "yyy@chatroom"]）
        Returns:
            Dict: 群详细信息
        """
        url = f"{self.base_url}/group/GetChatRoomInfo"
        json_data = {"ChatRoomWxIdList": chatroom_wxid_list}
        return post_json(base_url=url, token=key, data=json_data)

    def scan_into_url_group(self, key: str, url: str) -> Dict:
        """
        扫码入群
        Args:
            key: 账号唯一标识
            url: 群邀请链接或二维码URL
        Returns:
            Dict: 入群结果
        """
        api_url = f"{self.base_url}/group/ScanIntoUrlGroup"
        json_data = {"Url": url}
        return post_json(base_url=api_url, token=key, data=json_data)

    def send_pat(self, key: str, chatroom_name: str, to_user_name: str, scene: int = 0) -> Dict:
        """
        群拍一拍功能
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            to_user_name: 要拍的用户wxid
            scene: 场景值，默认为0 (int64)
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/group/SendPat"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_name,
            "Scene": scene
        }
        return post_json(base_url=url, token=key, data=json_data)
