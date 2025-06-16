from libs.wechatpad_api.util.http_util import post_json, async_request, get_json
from typing import List, Dict, Any, Optional
from datetime import datetime


class FriendApi:
    """联系人API类，处理所有与联系人相关的操作
    
    该类封装了微信Pad Pro联系人相关的所有API接口，包括：
    - 好友管理(添加、删除、修改备注等)
    - 联系人查询(搜索、获取列表等)
    - 群组管理(获取群列表等)
    - 公众号管理(获取公众号列表等)
    
    所有方法都需要提供base_url和token进行初始化
    """

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token

    def agree_add(self, key: str, user_name: str, verify_content: str = "", scene: int = 3, opcode: int = 2) -> Dict:
        """
        同意好友请求
        Args:
            key: 账号唯一标识
            user_name: 要同意的用户名
            verify_content: 验证信息内容
            scene: 添加来源(参见verify_user方法的scene参数说明)
            opcode: 操作类型(参见verify_user方法的opcode参数说明)
        Returns:
            Dict: 操作结果
        """
        url = f"{self.base_url}/friend/VerifyUser"
        json_data = {
            "UserName": user_name,
            "VerifyContent": verify_content,
            "OpCode": opcode,
            "Scene": scene
        }
        return post_json(base_url=url, token=key, data=json_data)

    def batch_get_contact(self, key: str, room_wxid_list: List[str], user_names: List[str]) -> Dict:
        """
        批量获取联系人详情
        Args:
            key: 账号唯一标识
            room_wxid_list: 群聊ID列表
            user_names: 用户名列表
        Returns:
            Dict: 联系人详情信息
        """
        url = f"{self.base_url}/friend/GetContactDetailsList"
        json_data = {
            "RoomWxIDList": room_wxid_list,
            "UserNames": user_names
        }
        return post_json(base_url=url, token=key, data=json_data)

    def del_contact(self, key: str, del_user_name: str) -> Dict:
        """
        删除好友
        Args:
            key: 账号唯一标识
            del_user_name: 要删除的用户名
        Returns:
            Dict: 删除操作结果
        """
        url = f"{self.base_url}/friend/DelContact"
        json_data = {"DelUserName": del_user_name}
        return post_json(base_url=url, token=key, data=json_data)

    def get_contact_list(self, key: str, current_wxcontact_seq: int = 0, current_chatroom_contact_seq: int = 0) -> Dict:
        """
        获取全部联系人
        Args:
            key: 账号唯一标识
            current_wxcontact_seq: 当前联系人序列号(用于增量同步)
            current_chatroom_contact_seq: 当前群聊联系人序列号(用于增量同步)
        Returns:
            Dict: 联系人列表
        """
        url = f"{self.base_url}/friend/GetContactList"
        json_data = {
            "CurrentWxcontactSeq": current_wxcontact_seq,
            "CurrentChatRoomContactSeq": current_chatroom_contact_seq
        }
        return post_json(base_url=url, token=key, data=json_data)

    def get_friend_list(self, key: str) -> Dict:
        """
        获取好友列表
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 好友列表信息
        """
        url = f"{self.base_url}/friend/GetFriendList"
        return get_json(base_url=url, token=key)

    def get_friend_relation(self, key: str, user_name: str) -> Dict:
        """
        获取好友关系
        Args:
            key: 账号唯一标识
            user_name: 要查询的用户名
        Returns:
            Dict: 好友关系信息
        """
        url = f"{self.base_url}/friend/GetFriendRelation"
        json_data = {"UserName": user_name}
        return post_json(base_url=url, token=key, data=json_data)

    def get_group_list(self, key: str) -> Dict:
        """
        获取保存的群聊列表
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 群组列表信息
        """
        url = f"{self.base_url}/friend/GroupList"
        return get_json(base_url=url, token=key)

    def search_contact(self, key: str, user_name: str, from_scene: int, tg: str = "", op_code: int = 1, search_scene: int = 1) -> Dict:
        """
        搜索联系人
        Args:
            key: 账号唯一标识
            user_name: 要搜索的内容(微信号、手机号、QQ号等)
            from_scene: 来源场景
            tg: 附加参数
            op_code: 操作类型
            search_scene: 搜索场景
        Returns:
            Dict: 搜索结果
        """
        url = f"{self.base_url}/friend/SearchContact"
        json_data = {
            "UserName": user_name,
            "FromScene": from_scene,
            "Tg": tg,
            "OpCode": op_code,
            "SearchScene": search_scene
        }
        return post_json(base_url=url, token=key, data=json_data)

    def upload_mcontact(self, key: str, mobile_list: List[str]) -> Dict:
        """
        上传手机通讯录好友
        Args:
            key: 账号唯一标识
            mobile_list: 手机号列表
        Returns:
            Dict: 上传操作结果
        """
        url = f"{self.base_url}/friend/UploadMContact"
        json_data = {"MobileList": mobile_list}
        return post_json(base_url=url, token=key, data=json_data)

    def verify_user(self, key: str, user_name: str, verify_content: str = "", opcode: int = 2, scene: int = 3,
                    chat_room_user_name: str = "", v3: str = "", v4: str = "") -> Dict:
        """
        验证好友/添加好友
        Args:
            key: 账号唯一标识
            user_name: 要验证的用户名
            verify_content: 验证信息内容
            opcode: 操作类型(1:免验证发送请求, 2:添加好友/发送验证申请, 3:同意好友/通过好友验证, 4:拒绝好友)
            scene: 添加来源(1:QQ, 2:邮箱, 3:微信号, 4:QQ好友, 8:来自群聊, 13:通讯录, 14:群聊, 15:手机号, 18:附近的人, 25:漂流瓶, 29:摇一摇, 30:二维码)
            chat_room_user_name: 通过群来添加好友时需要设置的群ID
            v3: V3用户名数据(SearchContact请求返回的UserValue)
            v4: V4校验数据(SearchContact请求返回的AntispamTicket)
        Returns:
            Dict: 验证结果
        """
        url = f"{self.base_url}/friend/VerifyUser"
        json_data = {
            "UserName": user_name,
            "VerifyContent": verify_content,
            "OpCode": opcode,
            "Scene": scene,
            "ChatRoomUserName": chat_room_user_name,
            "V3": v3,
            "V4": v4
        }
        return post_json(base_url=url, token=key, data=json_data)

    def get_gh_list(self, key: str) -> Dict:
        """
        获取关注的公众号列表
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 公众号列表信息
        """
        url = f"{self.base_url}/friend/GetGHList"
        return get_json(base_url=url, token=key)

    def get_mfriend(self, key: str) -> Dict:
        """
        获取手机通讯录好友
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 手机通讯录好友信息
        """
        url = f"{self.base_url}/friend/GetMFriend"
        return get_json(base_url=url, token=key)
