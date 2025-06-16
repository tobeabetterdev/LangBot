from typing import Dict, List, Optional
from libs.wechatpad_api.api.login import LoginApi
from libs.wechatpad_api.api.friend import FriendApi
from libs.wechatpad_api.api.message import MessageApi
from libs.wechatpad_api.api.admin import AdminApi
from libs.wechatpad_api.api.official_account import OfficialAccountApi
from libs.wechatpad_api.api.sync_message import SyncMessageApi
from libs.wechatpad_api.api.user import UserApi
from libs.wechatpad_api.api.equipment import EquipmentApi
from libs.wechatpad_api.api.favor import FavorApi
from libs.wechatpad_api.api.finder import FinderApi
from libs.wechatpad_api.api.group import GroupApi
from libs.wechatpad_api.api.label import LabelApi
from libs.wechatpad_api.api.other import OtherApi
from libs.wechatpad_api.api.pay import PayApi
from libs.wechatpad_api.api.qy import QyApi
from libs.wechatpad_api.api.sns import SnsApi

class WeChatPadClient:
    def __init__(self, base_url: str, token: Optional[str] = None, logger=None):
        self._login_api = LoginApi(base_url, token)
        self._friend_api = FriendApi(base_url, token)
        self._message_api = MessageApi(base_url, token)
        self._user_api = UserApi(base_url, token)
        self._admin_api = AdminApi(base_url, token)
        self._equipment_api = EquipmentApi(base_url, token)
        self._favor_api = FavorApi(base_url, token)
        self._finder_api = FinderApi(base_url, token)
        self._group_api = GroupApi(base_url, token)
        self._label_api = LabelApi(base_url, token)
        self._official_account_api = OfficialAccountApi(base_url, token)
        self._other_api = OtherApi(base_url, token)
        self._pay_api = PayApi(base_url, token)
        self._qy_api = QyApi(base_url, token)
        self._sns_api = SnsApi(base_url, token)
        self._sync_message_api = SyncMessageApi(base_url, token)
        self.logger = logger
        self.token = token

    # LoginApi methods
    def get_login_qr(self, proxy: str = "") -> Dict:
        """
        获取登录二维码(异地IP用代理)
        Args:
            proxy: socks代理，例如：socks5://username:password@ipv4:port
        Returns:
            Dict: 包含二维码信息的字典
        """
        return self._login_api.get_login_qr(self.token, Proxy=proxy)

    def awaken_login(self, proxy: str = "") -> Dict:
        """
        唤醒登录(只限扫码登录)
        Args:
            proxy: socks代理，例如：socks5://username:password@ipv4:port
        Returns:
            Dict: 唤醒登录操作的结果
        """
        return self._login_api.wake_up_login(self.token, Proxy=proxy)

    def logout(self) -> Dict:
        """
        退出登录
        Returns:
            Dict: 退出登录操作的结果
        """
        return self._login_api.logout(self.token)

    def get_login_status(self) -> Dict:
        """
        获取在线状态
        Returns:
            Dict: 包含登录状态信息的字典
        """
        return self._login_api.get_login_status(self.token)

    def check_can_set_alias(self) -> Dict:
        """
        检测微信登录环境
        Returns:
            Dict: 检测结果的字典
        """
        return self._login_api.check_can_set_alias(self.token)

    def get_62_data(self) -> Dict:
        """
        提取62数据
        Returns:
            Dict: 62数据的字典
        """
        return self._login_api.get_62_data(self.token)

    def get_iwx_connect(self) -> Dict:
        """
        打印链接数量
        Returns:
            Dict: 链接数量的字典
        """
        return self._login_api.get_iwx_connect(self.token)

    def get_init_status(self) -> Dict:
        """
        初始化状态
        Returns:
            Dict: 初始化状态的字典
        """
        return self._login_api.get_init_status(self.token)

    def show_qr_code(self) -> Dict:
        """
        HTML展示登录二维码
        Returns:
            Dict: HTML二维码信息的字典
        """
        return self._login_api.show_qr_code(self.token)

    def sms_login(self, device_info: Dict, login_data: str, password: str, proxy: str = "", ticket: str = "", type: int = 0, username: str = "") -> Dict:
        """
        短信登录
        Args:
            device_info: 设备信息
            login_data: 62数据/A16数据
            password: 微信密码
            proxy: socks代理，例如：socks5://username:password@ipv4:port
            ticket: SMS短信验证码
            type: 类型
            username: 手机号
        Returns:
            Dict: 短信登录操作的结果
        """
        return self._login_api.sms_login(self.token, device_info, login_data, password, proxy, ticket, type, username)

    def wx_bind_op_mobile_for_reg(self, op_code: int, phone_number: str, proxy: str = "", reg: int = 0, verify_code: str = "") -> Dict:
        """
        获取验证码
        Args:
            op_code: 操作类型
            phone_number: 手机号
            proxy: 代理
            reg: 注册标识
            verify_code: 验证码
        Returns:
            Dict: 获取验证码操作的结果
        """
        return self._login_api.wx_bind_op_mobile_for_reg(self.token, op_code, phone_number, proxy, reg, verify_code)

    def a16_login(self, device_info: Dict, login_data: str, password: str, proxy: str = "", ticket: str = "", type: int = 0, username: str = "") -> Dict:
        """
        数据登录
        Args:
            device_info: 设备信息
            login_data: 62数据/A16数据
            password: 微信密码
            proxy: socks代理，例如：socks5://username:password@ipv4:port
            ticket: SMS短信验证码
            type: 类型
            username: 手机号
        Returns:
            Dict: 数据登录操作的结果
        """
        return self._login_api.a16_login(self.token, device_info, login_data, password, proxy, ticket, type, username)

    def get_login_qr_code_new_x(self, check: bool = False, proxy: str = "") -> Dict:
        """
        获取登录二维码(绕过验证码)
        Args:
            check: 修改代理时(SetProxy接口) 是否发送检测代理请求(可能导致请求超时)
            proxy: socks代理，例如：socks5://username:password@ipv4:port
        Returns:
            Dict: 包含二维码信息的字典
        """
        return self._login_api.get_login_qr_code_new_x(self.token, check, proxy)

    def login_new(self, device_info: Dict, login_data: str, password: str, proxy: str = "", ticket: str = "", type: int = 0, username: str = "") -> Dict:
        """
        62LoginNew新疆号登录
        Args:
            device_info: 设备信息
            login_data: 62数据/A16数据
            password: 微信密码
            proxy: socks代理，例如：socks5://username:password@ipv4:port
            ticket: SMS短信验证码
            type: 类型
            username: 手机号
        Returns:
            Dict: 登录操作的结果
        """
        return self._login_api.login_new(self.token, device_info, login_data, password, proxy, ticket, type, username)

    def phone_device_login(self, url: str = "") -> Dict:
        """
        辅助新手机登录
        Args:
            url: URL
        Returns:
            Dict: 辅助新手机登录操作的结果
        """
        return self._login_api.phone_device_login(self.token, url)

    # FriendApi methods
    def agree_add_friend(self, user_name: str, verify_content: str = "", scene: int = 3, opcode: int = 2) -> Dict:
        """
        同意好友请求
        Args:
            user_name: 要同意的用户名
            verify_content: 验证信息内容
            scene: 添加来源(参见verify_user方法的scene参数说明)
            opcode: 操作类型(参见verify_user方法的opcode参数说明)
        Returns:
            Dict: 操作结果
        """
        return self._friend_api.agree_add(self.token, user_name, verify_content, scene, opcode)

    def batch_get_contact(self, room_wxid_list: List[str], user_names: List[str]) -> Dict:
        """
        批量获取联系人详情
        Args:
            room_wxid_list: 群聊ID列表
            user_names: 用户名列表
        Returns:
            Dict: 联系人详情信息
        """
        return self._friend_api.batch_get_contact(self.token, room_wxid_list, user_names)

    def del_contact(self, del_user_name: str) -> Dict:
        """
        删除好友
        Args:
            del_user_name: 要删除的用户名
        Returns:
            Dict: 删除操作结果
        """
        return self._friend_api.del_contact(self.token, del_user_name)

    def get_contact_list(self, current_wxcontact_seq: int = 0, current_chatroom_contact_seq: int = 0) -> Dict:
        """
        获取全部联系人
        Args:
            current_wxcontact_seq: 当前联系人序列号(用于增量同步)
            current_chatroom_contact_seq: 当前群聊联系人序列号(用于增量同步)
        Returns:
            Dict: 联系人列表
        """
        return self._friend_api.get_contact_list(self.token, current_wxcontact_seq, current_chatroom_contact_seq)

    def get_friend_list(self) -> Dict:
        """
        获取好友列表
        Returns:
            Dict: 好友列表信息
        """
        return self._friend_api.get_friend_list(self.token)

    def get_friend_relation(self, user_name: str) -> Dict:
        """
        获取好友关系
        Args:
            user_name: 要查询的用户名
        Returns:
            Dict: 好友关系信息
        """
        return self._friend_api.get_friend_relation(self.token, user_name)

    def get_group_list(self) -> Dict:
        """
        获取保存的群聊列表
        Returns:
            Dict: 群组列表信息
        """
        return self._friend_api.get_group_list(self.token)

    def search_contact(self, user_name: str, from_scene: int, tg: str = "", op_code: int = 1, search_scene: int = 1) -> Dict:
        """
        搜索联系人
        Args:
            user_name: 要搜索的内容(微信号、手机号、QQ号等)
            from_scene: 来源场景
            tg: 附加参数
            op_code: 操作类型
            search_scene: 搜索场景
        Returns:
            Dict: 搜索结果
        """
        return self._friend_api.search_contact(self.token, user_name, from_scene, tg, op_code, search_scene)

    def upload_mcontact(self, mobile_list: List[str]) -> Dict:
        """
        上传手机通讯录好友
        Args:
            mobile_list: 手机号列表
        Returns:
            Dict: 上传操作结果
        """
        return self._friend_api.upload_mcontact(self.token, mobile_list)

    def verify_user(self, user_name: str, verify_content: str = "", opcode: int = 2, scene: int = 3,
                    chat_room_user_name: str = "", v3: str = "", v4: str = "") -> Dict:
        """
        验证好友/添加好友
        Args:
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
        return self._friend_api.verify_user(self.token, user_name, verify_content, opcode, scene, chat_room_user_name, v3, v4)

    def get_gh_list(self) -> Dict:
        """
        获取关注的公众号列表
        Returns:
            Dict: 公众号列表信息
        """
        return self._friend_api.get_gh_list(self.token)

    def get_mfriend(self) -> Dict:
        """
        获取手机通讯录好友
        Returns:
            Dict: 手机通讯录好友信息
        """
        return self._friend_api.get_mfriend(self.token)

    # MessageApi methods
    def send_text_message(self, to_wxid: str, content: str, at_wxid_list: Optional[List[str]] = None) -> Dict:
        """
        发送文本消息
        Args:
            to_wxid: 接收者wxid
            content: 文本类型消息时内容
            at_wxid_list: 发送艾特消息时的 wxid 列表 (可选)
        Returns:
            Dict: 发送消息操作的结果
        """
        return self._message_api.send_text_message(self.token, to_wxid, content, at_wxid_list)

    def send_image_message(self, to_wxid: str, image_content: str, at_wxid_list: Optional[List[str]] = None) -> Dict:
        """
        发送图片消息
        Args:
            to_wxid: 接收者wxid
            image_content: 图片类型消息时图片的 base64 编码
            at_wxid_list: 发送艾特消息时的 wxid 列表 (可选)
        Returns:
            Dict: 发送图片消息操作的结果
        """
        return self._message_api.send_image_message(self.token, to_wxid, image_content, at_wxid_list)

    def send_voice_message(self, to_user_name: str, voice_data: str, voice_format: int, voice_second: int) -> Dict:
        """
        发送语音
        Args:
            to_user_name: 接收者wxid
            voice_data: 语音数据 (Base64编码)
            voice_format: 语音格式
            voice_second: 语音时长 (秒)
        Returns:
            Dict: 发送语音操作的结果
        """
        return self._message_api.send_voice(self.token, to_user_name=to_user_name, voice_data=voice_data, voice_format=voice_format, voice_second=voice_second)

    def share_card_message(self, to_user_name: str, card_wx_id: str, card_nick_name: str, card_flag: int, card_alias: str = "") -> Dict:
        """
        分享名片消息
        Args:
            to_user_name: 消息接收者
            card_wx_id: 名片wxid
            card_nick_name: 名片昵称
            card_flag: 名片CertFlag (0:个人名片 24:公众号名片)
            card_alias: 名片别名(发送公众号名片时留空)
        Returns:
            Dict: 分享名片消息操作的结果
        """
        return self._message_api.share_card_message(self.token, to_user_name, card_wx_id, card_nick_name, card_flag, card_alias)

    def send_emoji_message(self, emoji_list: List[Dict]) -> Dict:
        """
        发送表情
        Args:
            emoji_list: 表情列表，每个元素为包含 "EmojiMd5", "EmojiSize", "ToUserName" 的字典
        Returns:
            Dict: 发送表情操作的结果
        """
        return self._message_api.send_emoji_message(self.token, emoji_list)

    def send_app_message(self, app_list: List[Dict]) -> Dict:
        """
        发送App消息
        Args:
            app_list: App消息列表，每个元素为包含 "ContentType", "ContentXML", "ToUserName" 的字典
        Returns:
            Dict: 发送App消息操作的结果
        """
        return self._message_api.send_app_message(self.token, app_list)

    def revoke_msg(self, to_user_name: str, client_msg_id: int, create_time: int, new_msg_id: str) -> Dict:
        """
        撤销消息
        Args:
            to_user_name: 接收者wxid
            client_msg_id: 客户端消息ID
            create_time: 创建时间
            new_msg_id: 新消息ID
        Returns:
            Dict: 撤销消息操作的结果
        """
        return self._message_api.revoke_msg(self.token, to_user_name, client_msg_id, create_time, new_msg_id)

    def add_message_mgr(self, msg_item: List[Dict]) -> Dict:
        """
        添加要发送的文本消息进入管理器
        Args:
            msg_item: 消息体数组，格式同SendMessageModel
        Returns:
            Dict: 添加消息到管理器操作的结果
        """
        return self._message_api.add_message_mgr(self.token, msg_item)

    def cdn_upload_video(self, thumb_data: str, to_user_name: str, video_data: List[int]) -> Dict:
        """
        上传视频
        Args:
            thumb_data: ThumbData (Base64编码)
            to_user_name: ToUserName
            video_data: 视频数据 (字节数组)
        Returns:
            Dict: 上传视频操作的结果
        """
        return self._message_api.cdn_upload_video(self.token, thumb_data, to_user_name, video_data)

    def forward_emoji(self, emoji_list: List[Dict]) -> Dict:
        """
        转发表情，包含动图
        Args:
            emoji_list: 表情列表，每个元素为包含 "EmojiMd5", "EmojiSize", "ToUserName" 的字典
        Returns:
            Dict: 转发表情操作的结果
        """
        return self._message_api.forward_emoji(self.token, emoji_list)

    def forward_image_message(self, forward_image_list: List[Dict]) -> Dict:
        """
        转发图片
        Args:
            forward_image_list: 图片列表，每个元素为包含 "AesKey", "CdnMidImgSize", "CdnMidImgUrl", "CdnThumbImgSize", "ToUserName" 的字典
        Returns:
            Dict: 转发图片操作的结果
        """
        return self._message_api.forward_image_message(self.token, forward_image_list)

    def forward_video_message(self, forward_video_list: List[Dict]) -> Dict:
        """
        转发视频
        Args:
            forward_video_list: 视频列表，每个元素为包含 "AesKey", "CdnThumbLength", "CdnVideoUrl", "Length", "PlayLength", "ToUserName" 的字典
        Returns:
            Dict: 转发视频操作的结果
        """
        return self._message_api.forward_video_message(self.token, forward_video_list)

    def get_msg_big_img(self, from_user_name: str, msg_id: int, section: Dict, to_user_name: str, total_len: int, compress_type: int = 0) -> Dict:
        """
        获取图片(高清图片下载)
        Args:
            from_user_name: 下载图片时，图片消息的发送者
            msg_id: 消息ID (注意是msg_id 不是new_msg_id)
            section: 当前要获取的数据分包 {"DataLen": 数据分包长度, "StartPos": 数据分包开始位置}
            to_user_name: 下载图片时，图片消息的接收者
            total_len: 下载数据的总长度
            compress_type: 下载图片时，数据压缩类型(默认为0即可)
        Returns:
            Dict: 高清图片下载结果
        """
        return self._message_api.get_msg_big_img(self.token, from_user_name, msg_id, section, to_user_name, total_len, compress_type)

    def get_msg_video(self, from_user_name: str, msg_id: int, section: Dict, to_user_name: str, total_len: int) -> Dict:
        """
        获取视频(视频数据下载)
        Args:
            from_user_name: 下载视频时，视频消息的发送者
            msg_id: 消息ID (注意是msg_id 不是new_msg_id)
            section: 当前要获取的数据分包 {"DataLen": 数据分包长度, "StartPos": 数据分包开始位置}
            to_user_name: 下载视频时，视频消息的接收者
            total_len: 下载数据的总长度
        Returns:
            Dict: 视频数据下载结果
        """
        return self._message_api.get_msg_video(self.token, from_user_name, msg_id, section, to_user_name, total_len)

    def get_msg_voice(self, bufid: str, length: int, new_msg_id: str, to_user_name: str) -> Dict:
        """
        下载语音消息
        Args:
            bufid: Bufid
            length: Length
            new_msg_id: NewMsgId
            to_user_name: ToUserName
        Returns:
            Dict: 语音消息下载结果
        """
        return self._message_api.get_msg_voice(self.token, bufid, length, new_msg_id, to_user_name)

    def group_mass_msg_image(self, image_base64: str, to_user_name: List[str]) -> Dict:
        """
        群发图片
        Args:
            image_base64: 图片Base64编码
            to_user_name: 接收者wxid列表
        Returns:
            Dict: 群发图片操作的结果
        """
        return self._message_api.group_mass_msg_image(self.token, image_base64, to_user_name)

    def group_mass_msg_text(self, content: str, to_user_name: List[str]) -> Dict:
        """
        群发接口 (群发文本消息)
        Args:
            content: 消息内容
            to_user_name: 接收者wxid列表
        Returns:
            Dict: 群发文本消息操作的结果
        """
        return self._message_api.group_mass_msg_text(self.token, content, to_user_name)

    def http_sync_msg(self, count: int = 0) -> Dict:
        """
        同步消息, HTTP-轮询方式
        Args:
            count: 同步几条消息; 接收空请求体, 默认为0, 同步所有消息
        Returns:
            Dict: 同步消息操作的结果
        """
        return self._message_api.http_sync_msg(self.token, count)

    def new_sync_history_message(self) -> Dict:
        """
        同步历史消息
        Returns:
            Dict: 同步历史消息操作的结果
        """
        return self._message_api.new_sync_history_message(self.token)

    def revoke_msg_new(self, client_msg_id: int, create_time: int, new_msg_id: str, to_user_name: str) -> Dict:
        """
        撤回消息（New）
        Args:
            client_msg_id: 客户端消息ID
            create_time: 创建时间
            new_msg_id: 新消息ID
            to_user_name: 接收者wxid
        Returns:
            Dict: 撤回消息操作的结果
        """
        return self._message_api.revoke_msg_new(self.token, client_msg_id, create_time, new_msg_id, to_user_name)

    # UserApi methods
    def get_profile(self) -> Dict:
        """
        获取个人资料信息
        Returns:
            Dict: 包含个人资料信息的字典
        """
        return self._user_api.get_profile(self.token)

    def get_qr_code(self, recover: bool = True, style: int = 8) -> Dict:
        """
        获取我的二维码
        Args:
            recover: 保持默认值, 无需修改
            style: 个人二维码样式: 可设置为8, 其余自行探索
        Returns:
            Dict: 包含二维码信息的字典
        """
        return self._user_api.get_qr_code(self.token, recover=recover, style=style)

    def get_safety_info(self) -> Dict:
        """
        获取安全设备列表
        Returns:
            Dict: 包含安全设备列表的字典
        """
        return self._user_api.get_safety_info(self.token)

    async def update_head_img(self, head_img_base64: str) -> Dict:
        """
        上传头像
        Args:
            head_img_base64: 头像图片的Base64编码
        Returns:
            Dict: 上传头像操作的结果
        """
        return await self._user_api.update_head_img(self.token, head_img_base64)

    def change_pwd(self, new_pass: str, old_pass_param: str, op_code: int) -> Dict:
        """
        更改密码
        Args:
            new_pass: 新密码
            old_pass_param: 旧密码
            op_code: 操作类型
        Returns:
            Dict: 更改密码操作的结果
        """
        return self._user_api.change_pwd(self.token, new_pass, old_pass_param, op_code)

    def modify_remark(self, remark_name: str, user_name: str) -> Dict:
        """
        修改备注
        Args:
            remark_name: 备注名称
            user_name: 用户名
        Returns:
            Dict: 修改备注操作的结果
        """
        return self._user_api.modify_remark(self.token, remark_name, user_name)

    def modify_user_info(self, city: str = "", country: str = "", init_flag: int = 0,
                         nick_name: str = "", province: str = "", sex: int = 0, signature: str = "") -> Dict:
        """
        修改资料
        Args:
            city: 城市
            country: 国家
            init_flag: 初始化标志
            nick_name: 昵称
            province: 省份
            sex: 性别 (0: 未知, 1: 男, 2: 女)
            signature: 签名
        Returns:
            Dict: 修改资料操作的结果
        """
        return self._user_api.modify_user_info(self.token, city, country, init_flag, nick_name, province, sex, signature)

    def set_function_switch(self, function: int, value: int) -> Dict:
        """
        设置添加我的方式
        Args:
            function: 功能类型
            value: 值
        Returns:
            Dict: 设置功能开关操作的结果
        """
        return self._user_api.set_function_switch(self.token, function, value)

    def set_nick_name(self, scene: int, val: str) -> Dict:
        """
        设置昵称
        Args:
            scene: 场景
            val: 昵称值
        Returns:
            Dict: 设置昵称操作的结果
        """
        return self._user_api.set_nick_name(self.token, scene, val)

    def set_proxy(self, check: bool = False, proxy: str = "") -> Dict:
        """
        修改Socks5代理
        Args:
            check: 是否发送检测代理请求(可能导致请求超时)
            proxy: socks代理，例如：socks5://username:password@ipv4:port
        Returns:
            Dict: 设置代理操作的结果
        """
        return self._user_api.set_proxy(self.token, check, proxy)

    def set_send_pat(self, value: str) -> Dict:
        """
        设置拍一拍名称
        Args:
            value: 拍一拍名称
        Returns:
            Dict: 设置拍一拍名称操作的结果
        """
        return self._user_api.set_send_pat(self.token, value)

    def set_sex_dq(self, city: str = "", country: str = "", province: str = "", sex: int = 0) -> Dict:
        """
        修改性别
        Args:
            city: 城市
            country: 国家
            province: 省份
            sex: 性别 (0: 未知, 1: 男, 2: 女)
        Returns:
            Dict: 修改性别操作的结果
        """
        return self._user_api.set_sex_dq(self.token, city, country, province, sex)

    def set_signature(self, scene: int, val: str) -> Dict:
        """
        修改签名
        Args:
            scene: 场景
            val: 签名值
        Returns:
            Dict: 修改签名操作的结果
        """
        return self._user_api.set_signature(self.token, scene, val)

    def set_wechat(self, _alisa: str = "") -> Dict:
        """
        设置微信号
        Args:
            _alisa: 微信号
        Returns:
            Dict: 设置微信号操作的结果
        """
        return self._user_api.set_wechat(self.token, _alisa)

    def update_auto_pass(self, switch_type: int) -> Dict:
        """
        修改加好友需要验证属性
        Args:
            switch_type: 开关类型
        Returns:
            Dict: 修改加好友验证属性操作的结果
        """
        return self._user_api.update_auto_pass(self.token, switch_type)

    def update_nick_name(self, scene: int, val: str) -> Dict:
        """
        修改名称
        Args:
            scene: 场景
            val: 名称值
        Returns:
            Dict: 修改名称操作的结果
        """
        return self._user_api.update_nick_name(self.token, scene, val)

    # DownloadApi methods
    def cdn_download(self, aeskey: str, file_type: int, file_url: str) -> Dict:
        """
        下载 请求
        Args:
            aeskey: AesKey
            file_type: 文件类型
            file_url: 文件URL
        Returns:
            Dict: 下载请求操作的结果
        """
        return self._message_api.send_cdn_download(self.token, aeskey, file_type, file_url)

    def get_msg_voice_download(self, bufid: str, length: int, new_msg_id: str, to_user_name: str = "") -> Dict:
        """
        下载语音消息
        Args:
            bufid: Bufid
            length: Length
            new_msg_id: NewMsgId
            to_user_name: ToUserName
        Returns:
            Dict: 语音消息下载结果
        """
        return self._message_api.get_msg_voice(self.token, bufid, length, new_msg_id, to_user_name)

    # AdminApi methods
    def delay_auth_key(self, key: str, days: int = 30, expiry_date: str = "") -> Dict:
        """
        授权码延期
        Args:
            key: 要延期的 AuthKey
            days: AuthKey 的延期天数; Days 小于1默认设置为30
            expiry_date: AuthKey 的到期日期(例如: 2024-01-01); 与 Days 参数只能选其一(优先使用 ExpiryDate 参数)
        Returns:
            Dict: 操作结果
        """
        return self._admin_api.delay_auth_key(self.token, key, days, expiry_date)

    def delete_auth_key(self, key: str, opt: int = 0) -> Dict:
        """
        删除授权码
        Args:
            key: 要删除的 AuthKey
            opt: 删除操作 0:仅删除授权码 1:删除授权码相关的所有数据
        Returns:
            Dict: 操作结果
        """
        return self._admin_api.delete_auth_key(self.token, key, opt)

    def gen_auth_key1(self, count: int = 1, days: int = 365) -> Dict:
        """
        生成授权码(新设备)
        Args:
            count: 要生成 AuthKey 的个数; Count小于1默认设置为1
            days: AuthKey 的过期天数; Days小于1默认设置为30
        Returns:
            Dict: 生成结果
        """
        return self._admin_api.gen_auth_key1(self.token, count, days)

    def gen_auth_key2(self, key: str) -> Dict:
        """
        生成授权码(新设备) - GET接口
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 生成结果
        """
        return self._admin_api.gen_auth_key2(self.token, key)

    # EquipmentApi methods
    def get_bound_hard_device(self) -> Dict:
        """
        获取硬件设备情况
        Returns:
            Dict: 硬件设备信息
        """
        return self._equipment_api.get_bound_hard_device(self.token)

    def get_online_info(self) -> Dict:
        """
        获取在线设备信息
        Returns:
            Dict: 在线设备信息
        """
        return self._equipment_api.get_online_info(self.token)

    def del_safe_device(self, device_uuid: str) -> Dict:
        """
        删除安全设备
        Args:
            device_uuid: 要删除的设备UUID
        Returns:
            Dict: 操作结果
        """
        return self._equipment_api.del_safe_device(self.token, device_uuid)

    # FavorApi methods
    def batch_del_fav_item(self, fav_id: int, key_buf: str) -> Dict:
        """
        批量删除收藏
        Args:
            fav_id: 收藏ID
            key_buf: 解密密钥
        Returns:
            Dict: 操作结果
        """
        return self._favor_api.batch_del_fav_item(self.token, fav_id, key_buf)

    def fav_sync(self) -> Dict:
        """
        同步收藏
        Returns:
            Dict: 收藏同步结果
        """
        return self._favor_api.fav_sync(self.token)

    def get_fav_item_id(self, fav_id: int) -> Dict:
        """
        获取收藏详细
        Args:
            fav_id: 收藏ID
        Returns:
            Dict: 收藏详细信息
        """
        return self._favor_api.get_fav_item_id(self.token, fav_id)

    def get_fav_list(self, fav_id: int = 0, key_buf: str = "") -> Dict:
        """
        获取收藏list
        Args:
            fav_id: 收藏ID (可选，用于分页或特定查询)
            key_buf: KeyBuf (可选，用于分页或特定查询)
        Returns:
            Dict: 收藏列表信息
        """
        return self._favor_api.get_fav_list(self.token, fav_id, key_buf)

    # FinderApi methods
    def finder_follow(self, finder_user_name: str, op_type: int, poster_user_name: str = "",
                      ref_object_id: str = "", userver: int = 0, cook: str = "") -> Dict:
        """
        关注/取消视频号
        Args:
            finder_user_name: 视频号用户名
            op_type: 操作类型(1:关注 2:取消)
            poster_user_name: 发布者用户名
            ref_object_id: 参考对象ID
            userver: 用户版本号
            cook: 会话cookie
        Returns:
            Dict: 操作结果
        """
        return self._finder_api.finder_follow(self.token, finder_user_name, op_type, poster_user_name, ref_object_id, userver, cook)

    def finder_search(self, user_key: str, index: int = 0, userver: int = 0, uuid: str = "") -> Dict:
        """
        视频号搜索
        Args:
            user_key: 搜索关键词
            index: 分页索引
            userver: 用户版本号
            uuid: 会话UUID
        Returns:
            Dict: 搜索结果
        """
        return self._finder_api.finder_search(self.token, user_key, index, userver, uuid)

    def finder_user_prepare(self, userver: int = 0) -> Dict:
        """
        视频号中心准备
        Args:
            userver: 用户版本号
        Returns:
            Dict: 准备结果
        """
        return self._finder_api.finder_user_prepare(self.token, userver)

    # GroupApi methods
    def get_chatroom_member_detail(self, chatroom_name: str) -> Dict:
        """
        获取群成员详细信息
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
        Returns:
            Dict: 包含群成员详细信息的字典
        """
        return self._group_api.get_chatroom_member_detail(self.token, chatroom_name)

    def add_chat_room_members(self, chatroom_name: str, user_list: List[str]) -> Dict:
        """
        添加群成员 (邀请群成员)
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            user_list: 要添加的成员wxid列表
        Returns:
            Dict: 操作结果
        """
        return self._group_api.add_chat_room_members(self.token, chatroom_name, user_list)

    def del_chat_room_members(self, chatroom_name: str, user_list: List[str]) -> Dict:
        """
        删除群成员
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            user_list: 要删除的成员wxid列表
        Returns:
            Dict: 操作结果
        """
        return self._group_api.del_chat_room_members(self.token, chatroom_name, user_list)

    def add_chatroom_admin(self, chatroom_name: str, user_list: List[str]) -> Dict:
        """
        添加群管理员
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            user_list: 要设置为管理员的成员wxid列表
        Returns:
            Dict: 操作结果
        """
        return self._group_api.add_chatroom_admin(self.token, chatroom_name, user_list)

    def remove_chatroom_admin(self, chatroom_name: str, user_list: List[str]) -> Dict:
        """
        删除群管理员
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            user_list: 要移除管理员权限的成员wxid列表
        Returns:
            Dict: 操作结果
        """
        return self._group_api.remove_chatroom_admin(self.token, chatroom_name, user_list)

    def update_chatroom_announcement(self, chatroom_name: str, content: str) -> Dict:
        """
        设置群公告
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            content: 公告内容
        Returns:
            Dict: 操作结果
        """
        return self._group_api.update_chatroom_announcement(self.token, chatroom_name, content)

    def send_transfer_group_owner(self, chatroom_name: str, new_owner_user_name: str) -> Dict:
        """
        转让群
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            new_owner_user_name: 新群主的wxid
        Returns:
            Dict: 操作结果
        """
        return self._group_api.send_transfer_group_owner(self.token, chatroom_name, new_owner_user_name)

    def set_chatroom_access_verify(self, chatroom_name: str, enable: bool) -> Dict:
        """
        设置群聊邀请开关
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            enable: 是否开启验证（True为开启，False为关闭）
        Returns:
            Dict: 操作结果
        """
        return self._group_api.set_chatroom_access_verify(self.token, chatroom_name, enable)

    def get_group_list_group_api(self) -> Dict:
        """
        获取群列表
        Returns:
            Dict: 群列表信息
        """
        return self._group_api.get_group_list(self.token)

    def create_chat_room(self, topic: str, user_list: List[str]) -> Dict:
        """
        创建群请求
        Args:
            topic: 群聊主题
            user_list: 初始成员wxid列表
        Returns:
            Dict: 创建结果
        """
        return self._group_api.create_chat_room(self.token, topic, user_list)

    def quit_chatroom(self, chatroom_name: str) -> Dict:
        """
        退出群聊
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
        Returns:
            Dict: 操作结果
        """
        return self._group_api.quit_chatroom(self.token, chatroom_name)

    def get_chatroom_qrcode(self, chatroom_name: str) -> Dict:
        """
        获取群二维码
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
        Returns:
            Dict: 包含群二维码信息的字典
        """
        return self._group_api.get_chatroom_qrcode(self.token, chatroom_name)

    def set_chatroom_name(self, chatroom_name: str, nickname: str) -> Dict:
        """
        设置群昵称
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            nickname: 新的群昵称
        Returns:
            Dict: 操作结果
        """
        return self._group_api.set_chatroom_name(self.token, chatroom_name, nickname)

    def move_to_contract(self, chatroom_name: str, val: int) -> Dict:
        """
        获取群聊（MoveToContract）
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            val: 未知参数，根据接口文档为uint32类型
        Returns:
            Dict: 操作结果
        """
        return self._group_api.move_to_contract(self.token, chatroom_name, val)

    def get_chatroom_announcement(self, chatroom_name: str) -> Dict:
        """
        获取群公告
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
        Returns:
            Dict: 群公告内容
        """
        return self._group_api.get_chatroom_announcement(self.token, chatroom_name)

    def get_chatroom_info(self, chatroom_wxid_list: List[str]) -> Dict:
        """
        获取群详情
        Args:
            chatroom_wxid_list: 群聊ID列表（格式：["xxx@chatroom", "yyy@chatroom"]）
        Returns:
            Dict: 群详细信息
        """
        return self._group_api.get_chatroom_info(self.token, chatroom_wxid_list)

    def scan_into_url_group(self, url: str) -> Dict:
        """
        扫码入群
        Args:
            url: 群邀请链接或二维码URL
        Returns:
            Dict: 入群结果
        """
        return self._group_api.scan_into_url_group(self.token, url)

    def send_pat(self, chatroom_name: str, to_user_name: str, scene: int = 0) -> Dict:
        """
        群拍一拍功能
        Args:
            chatroom_name: 群聊ID（格式：xxx@chatroom）
            to_user_name: 要拍的用户wxid
            scene: 场景值，默认为0 (int64)
        Returns:
            Dict: 操作结果
        """
        return self._group_api.send_pat(self.token, chatroom_name, to_user_name, scene)

    # LabelApi methods
    def add_contact_label(self, label_id: str, label_name_list: List[str]) -> Dict:
        """
        添加列表
        Args:
            label_id: 标签ID
            label_name_list: 标签名称列表
        Returns:
            Dict: 操作结果
        """
        return self._label_api.add_contact_label(self.token, label_id, label_name_list)

    def del_contact_label(self, label_id: str) -> Dict:
        """
        删除标签
        Args:
            label_id: 要删除的标签ID
        Returns:
            Dict: 操作结果
        """
        return self._label_api.del_contact_label(self.token, label_id)

    def get_contact_label_list(self) -> Dict:
        """
        获取标签列表
        Returns:
            Dict: 标签列表信息
        """
        return self._label_api.get_contact_label_list(self.token)

    def modify_label(self, label_id: str, label_name_list: List[str]) -> Dict:
        """
        修改标签
        Args:
            label_id: 要修改的标签ID
            label_name_list: 新的标签名称列表
        Returns:
            Dict: 操作结果
        """
        return self._label_api.modify_label(self.token, label_id, label_name_list)

    def get_wx_friend_list_by_label(self, label_id: str) -> Dict:
        """
        获取标签下所有好友
        Args:
            label_id: 标签ID
        Returns:
            Dict: 标签下的好友列表
        """
        return self._label_api.get_wx_friend_list_by_label(self.token, label_id)

    # OfficialAccountApi methods
    def auth_mp_login(self, opcode: int, scene: int, url: str) -> Dict:
        """
        授权公众号登录
        Args:
            opcode: 操作码
            scene: 场景
            url: URL
        Returns:
            Dict: 授权公众号登录操作的结果
        """
        return self._official_account_api.auth_mp_login(self.token, opcode, scene, url)

    def follow_gh(self, gh_list: List[Dict]) -> Dict:
        """
        关注公众号
        Args:
            gh_list: 公众号列表，每个元素为包含 "Gh", "Scene" 的字典
        Returns:
            Dict: 关注公众号操作的结果
        """
        return self._official_account_api.follow_gh(self.token, gh_list)

    def get_a8_key(self, opcode: int, req_url: str, scene: int) -> Dict:
        """
        授权链接 (GetA8Key)
        Args:
            opcode: 操作码
            req_url: 请求URL
            scene: 场景
        Returns:
            Dict: 授权链接操作的结果
        """
        return self._official_account_api.get_a8_key(self.token, opcode, req_url, scene)

    def get_mp_a8_key(self, opcode: int, scene: int, url: str) -> Dict:
        """
        授权链接 (GetMpA8Key)
        Args:
            opcode: 操作码
            scene: 场景
            url: URL
        Returns:
            Dict: 授权链接操作的结果
        """
        return self._official_account_api.get_mp_a8_key(self.token, opcode, scene, url)

    def get_mp_history_message(self, url: str) -> Dict:
        """
        获取公众号历史消息
        Args:
            url: URL
        Returns:
            Dict: 公众号历史消息列表
        """
        return self._official_account_api.get_mp_history_message(self.token, url)

    def js_operate_wx_data(self, app_id: str, data: str = "", opt: int = 1, package_name: str = "", sdk_name: str = "") -> Dict:
        """
        小程序云函数操作
        Args:
            app_id: 应用ID
            data: 小程序云函数操作的 Data; json字符串, 注意必须是 json 字符串; 传空时默认值为: '{"with_credentials":true,"from_component":true,"data":{"lang":"zh_CN"},"api_name":"webapi_getuserinfo"}'
            opt: 小程序云函数操作的 Opt; 默认为1
            package_name: PackageName
            sdk_name: SdkName
        Returns:
            Dict: 小程序云函数操作的结果
        """
        return self._official_account_api.js_operate_wx_data(self.token, app_id, data, opt, package_name, sdk_name)

    def js_login(self, app_id: str, data: str = "", opt: int = 1, package_name: str = "", sdk_name: str = "") -> Dict:
        """
        授权小程序(返回授权后的code)
        Args:
            app_id: 应用ID
            data: 小程序云函数操作的 Data
            opt: 小程序云函数操作的 Opt
            package_name: PackageName
            sdk_name: SdkName
        Returns:
            Dict: 授权小程序操作的结果
        """
        return self._official_account_api.js_login(self.token, app_id, data, opt, package_name, sdk_name)

    def qr_connect_authorize(self, qr_url: str) -> Dict:
        """
        二维码授权请求
        Args:
            qr_url: 二维码URL
        Returns:
            Dict: 二维码授权请求操作的结果
        """
        return self._official_account_api.qr_connect_authorize(self.token, qr_url)

    def qr_connect_authorize_confirm(self, qr_url: str) -> Dict:
        """
        二维码授权确认
        Args:
            qr_url: 二维码URL
        Returns:
            Dict: 二维码授权确认操作的结果
        """
        return self._official_account_api.qr_connect_authorize_confirm(self.token, qr_url)

    def sdk_oauth_authorize(self, app_id: str, data: str = "", opt: int = 1, package_name: str = "", sdk_name: str = "") -> Dict:
        """
        应用授权
        Args:
            app_id: 应用ID
            data: 数据
            opt: Opt
            package_name: PackageName
            sdk_name: SdkName
        Returns:
            Dict: 应用授权操作的结果
        """
        return self._official_account_api.sdk_oauth_authorize(self.token, app_id, data, opt, package_name, sdk_name)

    # OtherApi methods
    def get_people_nearby(self, latitude: float, longitude: float) -> Dict:
        """
        查看附近的人
        Args:
            latitude: 纬度
            longitude: 经度
        Returns:
            Dict: 附近的人列表
        """
        return self._other_api.get_people_nearby(self.token, latitude, longitude)

    def get_redis_sync_msg(self) -> Dict:
        """
        获取缓存在redis中的消息
        Returns:
            Dict: Redis中的消息
        """
        return self._other_api.get_redis_sync_msg(self.token)

    def get_user_rank_like_count(self, rank_id: str) -> Dict:
        """
        获取步数排行数据列表
        Args:
            rank_id: 排行榜ID
        Returns:
            Dict: 步数排行数据
        """
        return self._other_api.get_user_rank_like_count(self.token, rank_id)

    def redis_memory(self) -> Dict:
        """
        内存管理
        Returns:
            Dict: 内存管理信息
        """
        return self._other_api.redis_memory(self.token)

    def update_step_number(self, number: int) -> Dict:
        """
        修改步数
        Args:
            number: 步数
        Returns:
            Dict: 修改步数操作的结果
        """
        return self._other_api.update_step_number(self.token, number)

    # PayApi methods
    def collect_money(self, invalid_time: str, to_user_name: str, transfer_id: str, transaction_id: str) -> Dict:
        """
        确定收款
        Args:
            invalid_time: 无效时间
            to_user_name: 接收者wxid
            transfer_id: 转账ID
            transaction_id: 交易ID
        Returns:
            Dict: 确定收款操作的结果
        """
        return self._pay_api.collect_money(self.token, invalid_time, to_user_name, transfer_id, transaction_id)

    def confirm_pre_transfer(self, bank_serial: str, bank_type: str, pay_password: str, req_key: str) -> Dict:
        """
        确认转账(客户端版本过低会无法转账)
        Args:
            bank_serial: 付款方式 Serial序列号
            bank_type: 付款方式 类型
            pay_password: 支付密码
            req_key: 创建转账返回的ReqKey
        Returns:
            Dict: 确认转账操作的结果
        """
        return self._pay_api.confirm_pre_transfer(self.token, bank_serial, bank_type, pay_password, req_key)

    def create_pre_transfer(self, description: str, fee: int, to_user_name: str) -> Dict:
        """
        创建转账
        Args:
            description: 转账备注
            fee: 转账金额(单位为分)
            to_user_name: 要转账用户的wxid
        Returns:
            Dict: 创建转账操作的结果
        """
        return self._pay_api.create_pre_transfer(self.token, description, fee, to_user_name)

    def generate_pay_qrcode(self, money: str, name: str) -> Dict:
        """
        生成自定义收款二维码
        Args:
            money: 金额(单位为分), 999 即为 9.99 元
            name: 收款备注
        Returns:
            Dict: 生成收款二维码操作的结果
        """
        return self._pay_api.generate_pay_qrcode(self.token, money, name)

    def get_band_card_list(self) -> Dict:
        """
        获取银行卡信息
        Returns:
            Dict: 银行卡信息列表
        """
        return self._pay_api.get_band_card_list(self.token)

    def get_red_envelopes_detail(self, hong_bao_item: Dict) -> Dict:
        """
        查看红包详情
        Args:
            hong_bao_item: 红包项，包含 NativeURL 等信息
        Returns:
            Dict: 红包详情
        """
        return self._pay_api.get_red_envelopes_detail(self.token, hong_bao_item)

    def get_red_packet_list(self, hong_bao_item: Dict, limit: int, native_url: str, offset: int) -> Dict:
        """
        查看红包领取列表
        Args:
            hong_bao_item: 红包项，包含 ChannelID, MsgType, SendID, SendUserName, ShowSourceMac, ShowWxPayTitle, Sign, Ver
            limit: 限制数量
            native_url: 原生URL
            offset: 偏移量
        Returns:
            Dict: 红包领取列表
        """
        return self._pay_api.get_red_packet_list(self.token, hong_bao_item, limit, native_url, offset)

    def open_red_envelopes(self, native_url: str) -> Dict:
        """
        拆红包
        Args:
            native_url: 红包的NativeURL
        Returns:
            Dict: 拆红包操作的结果
        """
        return self._pay_api.open_red_envelopes(self.token, native_url)

    def wx_create_red_packet(self, amount: int, content: str, count: int, from_type: int, red_type: int, username: str) -> Dict:
        """
        创建红包
        Args:
            amount: 每个红包的金额(单位为分, 最小为100); 总金额为 Amount*Count
            content: 红包的备注内容(祝福语)
            count: 红包个数(最少为1)
            from_type: InAway(0:群红包; 1:个人红包)
            red_type: 红包类型(0 普通红包; 1 拼手气红包; ? 专属红包)
            username: 红包接收者; wxid 或 群ID
        Returns:
            Dict: 创建红包操作的结果
        """
        return self._pay_api.wx_create_red_packet(self.token, amount, content, count, from_type, red_type, username)

    # QyApi methods
    def qw_accept_chatroom(self, link: str, opcode: int) -> Dict:
        """
        同意进企业群
        Args:
            link: 链接
            opcode: 操作码
        Returns:
            Dict: 同意进企业群操作的结果
        """
        return self._qy_api.qw_accept_chatroom(self.token, link, opcode)

    def qw_add_chatroom_member(self, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        直接拉朋友进企业群
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 要添加的成员wxid列表
        Returns:
            Dict: 添加群成员操作的结果
        """
        return self._qy_api.qw_add_chatroom_member(self.token, chatroom_name, to_user_list)

    def qw_admin_accept_join_chatroom_set(self, chatroom_name: str, p: int) -> Dict:
        """
        设定企业群管理审核进群
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            p: 参数P
        Returns:
            Dict: 设定企业群管理审核进群操作的结果
        """
        return self._qy_api.qw_admin_accept_join_chatroom_set(self.token, chatroom_name, p)

    def qw_apply_add_contact(self, content: str, user_name: str, v1: str) -> Dict:
        """
        向企业微信打招呼
        Args:
            content: 打招呼内容
            user_name: 用户名
            v1: V1数据
        Returns:
            Dict: 打招呼操作的结果
        """
        return self._qy_api.qw_apply_add_contact(self.token, content, user_name, v1)

    def qw_appoint_chatroom_admin(self, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        增加企业管理员
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 要增加的管理员wxid列表
        Returns:
            Dict: 增加企业管理员操作的结果
        """
        return self._qy_api.qw_appoint_chatroom_admin(self.token, chatroom_name, to_user_list)

    def qw_chatroom_announce(self, chatroom_name: str, content: str) -> Dict:
        """
        发布企业群公告
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            content: 公告内容
        Returns:
            Dict: 发布企业群公告操作的结果
        """
        return self._qy_api.qw_chatroom_announce(self.token, chatroom_name, content)

    def qw_chatroom_transfer_owner(self, chatroom_name: str, to_user_name: str) -> Dict:
        """
        转让企业群
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_name: 新群主的wxid
        Returns:
            Dict: 转让企业群操作的结果
        """
        return self._qy_api.qw_chatroom_transfer_owner(self.token, chatroom_name, to_user_name)

    def qw_contact(self, chat_room: str = "", t: str = "", to_user_name: str = "") -> Dict:
        """
        提取企业 wx 详情
        Args:
            chat_room: 群聊
            t: 类型
            to_user_name: 接收者wxid
        Returns:
            Dict: 企业微信详情的字典
        """
        return self._qy_api.qw_contact(self.token, chat_room, t, to_user_name)

    def qw_create_chatroom(self, to_user_list: List[str]) -> Dict:
        """
        创建企业群
        Args:
            to_user_list: 要创建群的成员wxid列表
        Returns:
            Dict: 创建企业群操作的结果
        """
        return self._qy_api.qw_create_chatroom(self.token, to_user_list)

    def qw_del_chatroom(self, chatroom_name: str, name: str) -> Dict:
        """
        删除企业群
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            name: 群名称
        Returns:
            Dict: 删除企业群操作的结果
        """
        return self._qy_api.qw_del_chatroom(self.token, chatroom_name, name)

    def qw_del_chatroom_admin(self, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        移除群管理员
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 要移除的管理员wxid列表
        Returns:
            Dict: 移除群管理员操作的结果
        """
        return self._qy_api.qw_del_chatroom_admin(self.token, chatroom_name, to_user_list)

    def qw_del_chatroom_member(self, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        删除企业群成员
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 要删除的成员wxid列表
        Returns:
            Dict: 删除企业群成员操作的结果
        """
        return self._qy_api.qw_del_chatroom_member(self.token, chatroom_name, to_user_list)

    def qw_get_chatroom_member(self, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        提取企业群全部成员
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 用户列表
        Returns:
            Dict: 企业群成员列表的字典
        """
        return self._qy_api.qw_get_chatroom_member(self.token, chatroom_name, to_user_list)

    def qw_get_chatroom_qr(self, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        提取企业群二维码
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 用户列表
        Returns:
            Dict: 企业群二维码的字典
        """
        return self._qy_api.qw_get_chatroom_qr(self.token, chatroom_name, to_user_list)

    def qw_get_chatroom_info(self, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        提取企业群名称公告设定等信息
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 用户列表
        Returns:
            Dict: 企业群信息的字典
        """
        return self._qy_api.qw_get_chatroom_info(self.token, chatroom_name, to_user_list)

    def qw_invite_chatroom_member(self, chatroom_name: str, to_user_list: List[str]) -> Dict:
        """
        发送群邀请链接
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            to_user_list: 用户列表
        Returns:
            Dict: 群邀请链接操作的结果
        """
        return self._qy_api.qw_invite_chatroom_member(self.token, chatroom_name, to_user_list)

    def qw_mod_chatroom_member_nick(self, chatroom_name: str, name: str) -> Dict:
        """
        修改成员在群中呢称
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            name: 昵称
        Returns:
            Dict: 修改成员群昵称操作的结果
        """
        return self._qy_api.qw_mod_chatroom_member_nick(self.token, chatroom_name, name)

    def qw_mod_chatroom_name(self, chatroom_name: str, name: str) -> Dict:
        """
        修改企业群名称
        Args:
            chatroom_name: 群聊ID：xxx@chatroom
            name: 新群名称
        Returns:
            Dict: 修改企业群名称操作的结果
        """
        return self._qy_api.qw_mod_chatroom_name(self.token, chatroom_name, name)

    def qw_remark(self, name: str, to_user_name: str) -> Dict:
        """
        备注企业 wxid
        Args:
            name: 备注名称
            to_user_name: 接收者wxid
        Returns:
            Dict: 备注企业wxid操作的结果
        """
        return self._qy_api.qw_remark(self.token, name, to_user_name)

    def qw_search_contact(self, from_scene: int, tg: str, user_name: str) -> Dict:
        """
        搜手机或企业对外名片链接提取验证
        Args:
            from_scene: 来源场景
            tg: Tg
            user_name: 用户名
        Returns:
            Dict: 搜索联系人操作的结果
        """
        return self._qy_api.qw_search_contact(self.token, from_scene, tg, user_name)

    def qw_sync_chatroom(self, key: str) -> Dict:
        """
        提取全部企业微信群-
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 企业微信群列表的字典
        """
        return self._qy_api.qw_sync_chatroom(self.token)

    def qw_sync_contact(self) -> Dict:
        """
        提取全部的企业通讯录
        Returns:
            Dict: 企业通讯录的字典
        """
        return self._qy_api.qw_sync_contact(self.token)

    # SnsApi methods
    def download_media(self, key: str, url: str) -> Dict:
        """
        下载朋友圈视频
        Args:
            key: 账号唯一标识
            url: 视频URL
        Returns:
            Dict: 下载朋友圈视频操作的结果
        """
        return self._sns_api.download_media(self.token, url)

    def get_collect_circle(self, black_list: Optional[List[str]] = None, fav_item_id: int = 0, location: Optional[Dict] = None, location_val: int = 0, source_id: str = "") -> Dict:
        """
        获取收藏朋友圈详情
        Args:
            black_list: 不可见好友列表
            fav_item_id: 收藏项ID
            location: 位置信息
            location_val: 位置值
            source_id: 来源ID
        Returns:
            Dict: 收藏朋友圈详情
        """
        return self._sns_api.get_collect_circle(self.token, black_list, fav_item_id, location, location_val, source_id)

    def get_sns_sync(self) -> Dict:
        """
        同步朋友圈
        Returns:
            Dict: 朋友圈同步结果
        """
        return self._sns_api.get_sns_sync(self.token)

    def send_cdn_sns_video_upload_request(self) -> Dict:
        """
        上传朋友圈视频
        Returns:
            Dict: 上传朋友圈视频操作的结果
        """
        return self._sns_api.send_cdn_sns_video_upload_request(self.token)

    def send_fav_item_circle(self, black_list: Optional[List[str]] = None, fav_item_id: int = 0, location: Optional[Dict] = None, location_val: int = 0, source_id: str = "") -> Dict:
        """
        转发收藏朋友圈
        Args:
            black_list: 不可见好友列表
            fav_item_id: 收藏项ID
            location: 位置信息
            location_val: 位置值
            source_id: 来源ID
        Returns:
            Dict: 转发收藏朋友圈操作的结果
        """
        return self._sns_api.send_fav_item_circle(self.token, black_list, fav_item_id, location, location_val, source_id)

    def send_friend_circle(self, content: str = "", content_style: int = 0, content_url: str = "", description: str = "",
                           group_user_list: Optional[List[str]] = None, image_data_list: Optional[List[str]] = None,
                           location_info: Optional[Dict] = None, media_list: Optional[List[Dict]] = None,
                           privacy: int = 0, video_data_list: Optional[List[str]] = None, with_user_list: Optional[List[str]] = None) -> Dict:
        """
        发送朋友圈
        Args:
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
        return self._sns_api.send_friend_circle(self.token, content, content_style, content_url, description, group_user_list, image_data_list, location_info, media_list, privacy, video_data_list, with_user_list)

    def send_friend_circle_by_xml(self, action_info: Optional[Dict] = None, app_info: Optional[Dict] = None, content_desc: str = "",
                                  content_desc_scene: int = 0, content_desc_show_type: int = 0, content_object: Optional[Dict] = None,
                                  create_time: int = 0, _id: int = 0, location: Optional[Dict] = None, _private: int = 0,
                                  public_user_name: str = "", show_flag: int = 0, sight_folded: int = 0,
                                  source_nick_name: str = "", source_user_name: str = "", stat_ext_str: str = "",
                                  statistics_data: str = "", stream_video: Optional[Dict] = None, user_name: str = "") -> Dict:
        """
        发送朋友圈XML结构
        Args:
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
        return self._sns_api.send_friend_circle_by_xml(self.token, action_info, app_info, content_desc, content_desc_scene, content_desc_show_type, content_object, create_time, _id, location, _private, public_user_name, show_flag, sight_folded, source_nick_name, source_user_name, stat_ext_str, statistics_data, stream_video, user_name)

    def send_one_id_circle(self, black_list: Optional[List[str]] = None, id: str = "", location: Optional[Dict] = None, location_val: int = 0) -> Dict:
        """
        一键转发朋友圈
        Args:
            black_list: 黑名单
            id: ID
            location: 位置信息
            location_val: 位置值
        Returns:
            Dict: 一键转发朋友圈操作的结果
        """
        return self._sns_api.send_one_id_circle(self.token, black_list, id, location, location_val)

    def send_sns_comment(self, sns_comment_list: List[Dict], tx: bool) -> Dict:
        """
        点赞评论
        Args:
            sns_comment_list: 朋友圈评论列表，每个元素为包含 "Content", "CreateTime", "ItemID", "OpType", "ReplyCommentID", "ReplyItem", "ToUserName" 的字典
            tx: Tx
        Returns:
            Dict: 点赞评论操作的结果
        """
        return self._sns_api.send_sns_comment(self.token, sns_comment_list, tx)

    def send_sns_object_detail_by_id(self, black_list: Optional[List[str]] = None, id: str = "", location: Optional[Dict] = None, location_val: int = 0) -> Dict:
        """
        获取指定id朋友圈
        Args:
            black_list: 黑名单
            id: ID
            location: 位置信息
            location_val: 位置值
        Returns:
            Dict: 指定id朋友圈详情
        """
        return self._sns_api.send_sns_object_detail_by_id(self.token, black_list, id, location, location_val)

    def send_sns_object_op(self, sns_object_op_list: List[Dict]) -> Dict:
        """
        朋友圈操作
        Args:
            sns_object_op_list: 朋友圈操作列表，每个元素为包含 "Data", "DataLen", "Ext", "OpType", "SnsObjID" 的字典
        Returns:
            Dict: 朋友圈操作的结果
        """
        return self._sns_api.send_sns_object_op(self.token, sns_object_op_list)

    def send_sns_time_line(self, first_page_md5: str = "", max_id: int = 0, user_name: str = "") -> Dict:
        """
        获取朋友圈主页
        Args:
            first_page_md5: 第一页MD5
            max_id: 最大ID
            user_name: 用户名
        Returns:
            Dict: 朋友圈主页信息
        """
        return self._sns_api.send_sns_time_line(self.token, first_page_md5, max_id, user_name)

    def send_sns_user_page(self, first_page_md5: str = "", max_id: int = 0, user_name: str = "") -> Dict:
        """
        获取指定人朋友圈
        Args:
            first_page_md5: 第一页MD5
            max_id: 最大ID
            user_name: 用户名
        Returns:
            Dict: 指定人朋友圈信息
        """
        return self._sns_api.send_sns_user_page(self.token, first_page_md5, max_id, user_name)

    def set_background_image(self, url: str) -> Dict:
        """
        设置朋友圈背景图片
        Args:
            url: 背景图片URL
        Returns:
            Dict: 设置朋友圈背景图片操作的结果
        """
        return self._sns_api.set_background_image(self.token, url)

    def set_friend_circle_days(self, function: int, value: int) -> Dict:
        """
        设置朋友圈可见天数
        Args:
            function: 功能
            value: 值
        Returns:
            Dict: 设置朋友圈可见天数操作的结果
        """
        return self._sns_api.set_friend_circle_days(self.token, function, value)

    def upload_friend_circle_image(self, image_data_list: Optional[List[str]] = None, video_data_list: Optional[List[str]] = None) -> Dict:
        """
        上传图片信息 (朋友圈)
        Args:
            image_data_list: 图片数据列表 (Base64编码)
            video_data_list: 视频数据列表 (Base64编码)
        Returns:
            Dict: 上传图片信息操作的结果
        """
        return self._sns_api.upload_friend_circle_image(self.token, image_data_list, video_data_list)

    # SyncMessageApi methods
    def get_sync_msg(self, key: str) -> Dict:
        """
        同步消息，ws协议; 下面有【同步消息-HTTP-轮询方式】
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 同步消息操作的结果
        """
        return self._sync_message_api.get_sync_msg(self.token)
