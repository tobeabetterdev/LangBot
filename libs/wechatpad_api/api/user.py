from typing import Dict, List, Optional
from libs.wechatpad_api.util.http_util import post_json, async_request, get_json


class UserApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化UserApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def get_profile(self, key: str) -> Dict:
        """
        获取个人资料信息
        Returns:
            Dict: 包含个人资料信息的字典
        """
        url = f'{self.base_url}/user/GetProfile'
        return get_json(base_url=url, token=key)

    def get_qr_code(self, key: str, recover: bool = True, style: int = 8) -> Dict:
        """
        获取我的二维码
        Args:
            recover: 保持默认值, 无需修改
            style: 个人二维码样式: 可设置为8, 其余自行探索
        Returns:
            Dict: 包含二维码信息的字典
        """
        param = {
            "Recover": recover,
            "Style": style
        }
        url = f'{self.base_url}/user/GetMyQrCode'
        return post_json(base_url=url, token=key, data=param)

    def get_safety_info(self, key: str) -> Dict:
        """
        获取安全设备列表
        Returns:
            Dict: 包含安全设备列表的字典
        """
        url = f'{self.base_url}/equipment/GetSafetyInfo'
        return post_json(base_url=url, token=key)

    async def update_head_img(self, key: str, head_img_base64: str) -> Dict:
        """
        上传头像
        Args:
            head_img_base64: 头像图片的Base64编码
        Returns:
            Dict: 上传头像操作的结果
        """
        param = {
            "Base64": head_img_base64
        }
        url = f'{self.base_url}/user/UploadHeadImage'
        return await async_request(base_url=url, token_key=key, json=param)

    def change_pwd(self, key: str, new_pass: str, old_pass_param: str, op_code: int) -> Dict:
        """
        更改密码
        Args:
            new_pass: 新密码
            old_pass_param: 旧密码
            op_code: 操作类型
        Returns:
            Dict: 更改密码操作的结果
        """
        url = f"{self.base_url}/user/ChangePwd"
        json_data = {
            "NewPass": new_pass,
            "OldPass": old_pass_param,
            "OpCode": op_code
        }
        return post_json(base_url=url, token=key, data=json_data)

    def modify_remark(self, key: str, remark_name: str, user_name: str) -> Dict:
        """
        修改备注
        Args:
            remark_name: 备注名称
            user_name: 用户名
        Returns:
            Dict: 修改备注操作的结果
        """
        url = f"{self.base_url}/user/ModifyRemark"
        json_data = {
            "RemarkName": remark_name,
            "UserName": user_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def modify_user_info(self, key: str, city: str = "", country: str = "", init_flag: int = 0,
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
        url = f"{self.base_url}/user/ModifyUserInfo"
        json_data = {
            "City": city,
            "Country": country,
            "InitFlag": init_flag,
            "NickName": nick_name,
            "Province": province,
            "Sex": sex,
            "Signature": signature
        }
        return post_json(base_url=url, token=key, data=json_data)

    def set_function_switch(self, key: str, function: int, value: int) -> Dict:
        """
        设置添加我的方式
        Args:
            function: 功能类型
            value: 值
        Returns:
            Dict: 设置功能开关操作的结果
        """
        url = f"{self.base_url}/user/SetFunctionSwitch"
        json_data = {
            "Function": function,
            "Value": value
        }
        return post_json(base_url=url, token=key, data=json_data)

    def set_nick_name(self, key: str, scene: int, val: str) -> Dict:
        """
        设置昵称
        Args:
            scene: 场景
            val: 昵称值
        Returns:
            Dict: 设置昵称操作的结果
        """
        url = f"{self.base_url}/user/SetNickName"
        json_data = {
            "Scene": scene,
            "Val": val
        }
        return post_json(base_url=url, token=key, data=json_data)

    def set_proxy(self, key: str, check: bool = False, proxy: str = "") -> Dict:
        """
        修改Socks5代理
        Args:
            check: 是否发送检测代理请求(可能导致请求超时)
            proxy: socks代理，例如：socks5://username:password@ipv4:port
        Returns:
            Dict: 设置代理操作的结果
        """
        url = f"{self.base_url}/user/SetProxy"
        json_data = {
            "Check": check,
            "Proxy": proxy
        }
        return post_json(base_url=url, token=key, data=json_data)

    def set_send_pat(self, key: str, value: str) -> Dict:
        """
        设置拍一拍名称
        Args:
            value: 拍一拍名称
        Returns:
            Dict: 设置拍一拍名称操作的结果
        """
        url = f"{self.base_url}/user/SetSendPat"
        json_data = {
            "Value": value
        }
        return post_json(base_url=url, token=key, data=json_data)

    def set_sex_dq(self, key: str, city: str = "", country: str = "", province: str = "", sex: int = 0) -> Dict:
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
        url = f"{self.base_url}/user/SetSexDq"
        json_data = {
            "City": city,
            "Country": country,
            "Province": province,
            "Sex": sex
        }
        return post_json(base_url=url, token=key, data=json_data)

    def set_signature(self, key: str, scene: int, val: str) -> Dict:
        """
        修改签名
        Args:
            scene: 场景
            val: 签名值
        Returns:
            Dict: 修改签名操作的结果
        """
        url = f"{self.base_url}/user/SetSignature"
        json_data = {
            "Scene": scene,
            "Val": val
        }
        return post_json(base_url=url, token=key, data=json_data)

    def set_wechat(self, key: str, _alisa: str = "") -> Dict:
        """
        设置微信号
        Args:
            _alisa: 微信号
        Returns:
            Dict: 设置微信号操作的结果
        """
        url = f"{self.base_url}/user/SetWechat"
        json_data = {
            "Alisa": _alisa
        }
        return post_json(base_url=url, token=key, data=json_data)

    def update_auto_pass(self, key: str, switch_type: int) -> Dict:
        """
        修改加好友需要验证属性
        Args:
            switch_type: 开关类型
        Returns:
            Dict: 修改加好友验证属性操作的结果
        """
        url = f"{self.base_url}/user/UpdateAutoPass"
        json_data = {
            "SwitchType": switch_type
        }
        return post_json(base_url=url, token=key, data=json_data)

    def update_nick_name(self, key: str, scene: int, val: str) -> Dict:
        """
        修改名称
        Args:
            scene: 场景
            val: 名称值
        Returns:
            Dict: 修改名称操作的结果
        """
        url = f"{self.base_url}/user/UpdateNickName"
        json_data = {
            "Scene": scene,
            "Val": val
        }
        return post_json(base_url=url, token=key, data=json_data)