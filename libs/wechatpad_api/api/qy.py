from typing import Dict, List, Optional
from libs.wechatpad_api.util.http_util import post_json, async_request, get_json


class QyApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化QyApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def qw_accept_chatroom(self, key: str, link: str, opcode: int) -> Dict:
        """
        同意进企业群
        Args:
            key: 账号唯一标识
            link: 链接
            opcode: 操作码
        Returns:
            Dict: 同意进企业群操作的结果
        """
        url = f"{self.base_url}/qy/QWAcceptChatRoom"
        json_data = {
            "Link": link,
            "Opcode": opcode
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_add_chatroom_member(self, key: str, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        直接拉朋友进企业群
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 要添加的成员wxid列表
        Returns:
            Dict: 添加群成员操作的结果
        """
        url = f"{self.base_url}/qy/QWAddChatRoomMember"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_list
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_admin_accept_join_chatroom_set(self, key: str, chatroom_name: str, p: int) -> Dict:
        """
        设定企业群管理审核进群
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            p: 参数P
        Returns:
            Dict: 设定企业群管理审核进群操作的结果
        """
        url = f"{self.base_url}/qy/QWAdminAcceptJoinChatRoomSet"
        json_data = {
            "ChatRoomName": chatroom_name,
            "P": p
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_apply_add_contact(self, key: str, content: str, user_name: str, v1: str) -> Dict:
        """
        向企业微信打招呼
        Args:
            key: 账号唯一标识
            content: 打招呼内容
            user_name: 用户名
            v1: V1数据
        Returns:
            Dict: 打招呼操作的结果
        """
        url = f"{self.base_url}/qy/QWApplyAddContact"
        json_data = {
            "Content": content,
            "UserName": user_name,
            "V1": v1
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_appoint_chatroom_admin(self, key: str, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        增加企业管理员
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 要增加的管理员wxid列表
        Returns:
            Dict: 增加企业管理员操作的结果
        """
        url = f"{self.base_url}/qy/QWAppointChatRoomAdmin"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_list
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_chatroom_announce(self, key: str, chatroom_name: str, content: str) -> Dict:
        """
        发布企业群公告
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            content: 公告内容
        Returns:
            Dict: 发布企业群公告操作的结果
        """
        url = f"{self.base_url}/qy/QWChatRoomAnnounce"
        json_data = {
            "ChatRoomName": chatroom_name,
            "Content": content
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_chatroom_transfer_owner(self, key: str, chatroom_name: str, to_user_name: str) -> Dict:
        """
        转让企业群
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_name: 新群主的wxid
        Returns:
            Dict: 转让企业群操作的结果
        """
        url = f"{self.base_url}/qy/QWChatRoomTransferOwner"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_contact(self, key: str, chat_room: str = "", t: str = "", to_user_name: str = "") -> Dict:
        """
        提取企业 wx 详情
        Args:
            key: 账号唯一标识
            chat_room: 群聊
            t: 类型
            to_user_name: 接收者wxid
        Returns:
            Dict: 企业微信详情的字典
        """
        url = f"{self.base_url}/qy/QWContact"
        json_data = {
            "ChatRoom": chat_room,
            "T": t,
            "ToUserName": to_user_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_create_chatroom(self, key: str, to_user_list: List[str]) -> Dict:
        """
        创建企业群
        Args:
            key: 账号唯一标识
            to_user_list: 要创建群的成员wxid列表
        Returns:
            Dict: 创建企业群操作的结果
        """
        url = f"{self.base_url}/qy/QWCreateChatRoom"
        json_data = {
            "ToUserName": to_user_list
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_del_chatroom(self, key: str, chatroom_name: str, name: str) -> Dict:
        """
        删除企业群
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            name: 群名称
        Returns:
            Dict: 删除企业群操作的结果
        """
        url = f"{self.base_url}/qy/QWDelChatRoom"
        json_data = {
            "ChatRoomName": chatroom_name,
            "Name": name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_del_chatroom_admin(self, key: str, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        移除群管理员
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 要移除的管理员wxid列表
        Returns:
            Dict: 移除群管理员操作的结果
        """
        url = f"{self.base_url}/qy/QWDelChatRoomAdmin"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_list
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_del_chatroom_member(self, key: str, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        删除企业群成员
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 要删除的成员wxid列表
        Returns:
            Dict: 删除企业群成员操作的结果
        """
        url = f"{self.base_url}/qy/QWDelChatRoomMember"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_list
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_get_chatroom_member(self, key: str, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        提取企业群全部成员
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 用户列表
        Returns:
            Dict: 企业群成员列表的字典
        """
        url = f"{self.base_url}/qy/QWGetChatRoomMember"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_list
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_get_chatroom_qr(self, key: str, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        提取企业群二维码
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 用户列表
        Returns:
            Dict: 企业群二维码的字典
        """
        url = f"{self.base_url}/qy/QWGetChatRoomQR"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_list
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_get_chatroom_info(self, key: str, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        提取企业群名称公告设定等信息
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 用户列表
        Returns:
            Dict: 企业群信息的字典
        """
        url = f"{self.base_url}/qy/QWGetChatroomInfo"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_list
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_invite_chatroom_member(self, key: str, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        发送群邀请链接
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 用户列表
        Returns:
            Dict: 群邀请链接操作的结果
        """
        url = f"{self.base_url}/qy/QWInviteChatRoomMember"
        json_data = {
            "ChatRoomName": chatroom_name,
            "ToUserName": to_user_list
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_mod_chatroom_member_nick(self, key: str, chatroom_name: str, name: str) -> Dict:
        """
        修改成员在群中呢称
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            name: 昵称
        Returns:
            Dict: 修改成员群昵称操作的结果
        """
        url = f"{self.base_url}/qy/QWModChatRoomMemberNick"
        json_data = {
            "ChatRoomName": chatroom_name,
            "Name": name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_mod_chatroom_name(self, key: str, chatroom_name: str, name: str) -> Dict:
        """
        修改企业群名称
        Args:
            key: 账号唯一标识
            chatroom_name: 群聊ID：xxx@chatroom
            name: 新群名称
        Returns:
            Dict: 修改企业群名称操作的结果
        """
        url = f"{self.base_url}/qy/QWModChatRoomName"
        json_data = {
            "ChatRoomName": chatroom_name,
            "Name": name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_remark(self, key: str, name: str, to_user_name: str) -> Dict:
        """
        备注企业 wxid
        Args:
            key: 账号唯一标识
            name: 备注名称
            to_user_name: 接收者wxid
        Returns:
            Dict: 备注企业wxid操作的结果
        """
        url = f"{self.base_url}/qy/QWRemark"
        json_data = {
            "Name": name,
            "ToUserName": to_user_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_search_contact(self, key: str, from_scene: int, tg: str, user_name: str) -> Dict:
        """
        搜手机或企业对外名片链接提取验证
        Args:
            key: 账号唯一标识
            from_scene: 来源场景
            tg: Tg
            user_name: 用户名
        Returns:
            Dict: 搜索联系人操作的结果
        """
        url = f"{self.base_url}/qy/QWSearchContact"
        json_data = {
            "FromScene": from_scene,
            "Tg": tg,
            "UserName": user_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qw_sync_chatroom(self, key: str) -> Dict:
        """
        提取全部企业微信群-
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 企业微信群列表的字典
        """
        url = f"{self.base_url}/qy/QWSyncChatRoom"
        json_data = {}
        return post_json(base_url=url, token=key, data=json_data)

    def qw_sync_contact(self, key: str) -> Dict:
        """
        提取全部的企业通讯录
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 企业通讯录的字典
        """
        url = f"{self.base_url}/qy/QWSyncContact"
        return get_json(base_url=url, token=key)