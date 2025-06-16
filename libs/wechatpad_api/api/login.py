from typing import Dict, List, Optional
from libs.wechatpad_api.util.http_util import async_request, post_json, get_json

"""
微信登录API接口
包含所有/login/路径下的微信登录相关功能
"""
class LoginApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化LoginApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def get_login_qr(self, key: str, Proxy: str = "") -> Dict:
        """
        获取登录二维码(异地IP用代理)
        Args:
            key: 账号唯一标识
            Proxy: socks代理，例如：socks5://username:password@ipv4:port
        Returns:
            Dict: 包含二维码信息的字典
        """
        url = f"{self.base_url}/login/GetLoginQrCodeNew"
        check = False
        if Proxy:
            check = True
        json_data = {
            "Check": check,
            "Proxy": Proxy
        }
        return post_json(base_url=url, token=key, data=json_data)

    def get_login_status(self, key: str) -> Dict:
        """
        获取在线状态
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 包含登录状态信息的字典
        """
        url = f'{self.base_url}/login/GetLoginStatus'
        return get_json(base_url=url, token=key)

    def logout(self, key: str) -> Dict:
        """
        退出登录
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 退出登录操作的结果
        """
        url = f'{self.base_url}/login/LogOut'
        return get_json(base_url=url, token=key)

    def wake_up_login(self, key: str, Proxy: str = "") -> Dict:
        """
        唤醒登录(只限扫码登录)
        Args:
            key: 账号唯一标识
            Proxy: socks代理，例如：socks5://username:password@ipv4:port
        Returns:
            Dict: 唤醒登录操作的结果
        """
        url = f'{self.base_url}/login/WakeUpLogin'
        check = False
        if Proxy:
            check = True
        json_data = {
            "Check": check,
            "Proxy": Proxy
        }
        return post_json(base_url=url, token=key, data=json_data)

    def login(self, key: str) -> None:
        """
        处理登录逻辑，如果token失效则重新获取
        Args:
            key: 账号唯一标识
        """
        login_status = self.get_login_status(key=key)
        if login_status.get("Code") == 300 and login_status.get("Text") == "你已退出微信":
            print("token已经失效，请重新获取并设置")
            # 这里不再自动获取token，因为get_token方法已被移除，且获取token是AdminApi的职责
            # 外部调用者应负责获取并设置token
            self.token = None # 清空token，表示需要重新设置

    def check_can_set_alias(self, key: str) -> Dict:
        """
        检测微信登录环境
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 检测结果的字典
        """
        url = f"{self.base_url}/login/CheckCanSetAlias"
        return get_json(base_url=url, token=key)

    def get_62_data(self, key: str) -> Dict:
        """
        提取62数据
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 62数据的字典
        """
        url = f"{self.base_url}/login/Get62Data"
        return get_json(base_url=url, token=key)

    def get_iwx_connect(self, key: str) -> Dict:
        """
        打印链接数量
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 链接数量的字典
        """
        url = f"{self.base_url}/login/GetIWXConnect"
        return get_json(base_url=url, token=key)

    def get_init_status(self, key: str) -> Dict:
        """
        初始化状态
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 初始化状态的字典
        """
        url = f"{self.base_url}/login/GetInItStatus"
        return get_json(base_url=url, token=key)

    def show_qr_code(self, key: str) -> Dict:
        """
        HTML展示登录二维码
        Args:
            key: 账号唯一标识
        Returns:
            Dict: HTML二维码信息的字典
        """
        url = f"{self.base_url}/login/ShowQrCode"
        return get_json(base_url=url, token=key)

    def sms_login(self, key: str, device_info: Dict, login_data: str, password: str, proxy: str = "", ticket: str = "", type: int = 0, username: str = "") -> Dict:
        """
        短信登录
        Args:
            key: 账号唯一标识
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
        url = f"{self.base_url}/login/SmsLogin"
        json_data = {
            "DeviceInfo": device_info,
            "LoginData": login_data,
            "Password": password,
            "Proxy": proxy,
            "Ticket": ticket,
            "Type": type,
            "UserName": username
        }
        return post_json(base_url=url, token=key, data=json_data)

    def wx_bind_op_mobile_for_reg(self, key: str, op_code: int, phone_number: str, proxy: str = "", reg: int = 0, verify_code: str = "") -> Dict:
        """
        获取验证码
        Args:
            key: 账号唯一标识
            op_code: 操作类型
            phone_number: 手机号
            proxy: 代理
            reg: 注册标识
            verify_code: 验证码
        Returns:
            Dict: 获取验证码操作的结果
        """
        url = f"{self.base_url}/login/WxBindOpMobileForReg"
        json_data = {
            "OpCode": op_code,
            "PhoneNumber": phone_number,
            "Proxy": proxy,
            "Reg": reg,
            "VerifyCode": verify_code
        }
        return post_json(base_url=url, token=key, data=json_data)

    def a16_login(self, key: str, device_info: Dict, login_data: str, password: str, proxy: str = "", ticket: str = "", type: int = 0, username: str = "") -> Dict:
        """
        数据登录
        Args:
            key: 账号唯一标识
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
        url = f"{self.base_url}/login/A16Login"
        json_data = {
            "DeviceInfo": device_info,
            "LoginData": login_data,
            "Password": password,
            "Proxy": proxy,
            "Ticket": ticket,
            "Type": type,
            "UserName": username
        }
        return post_json(base_url=url, token=key, data=json_data)

    def get_login_qr_code_new_x(self, key: str, check: bool = False, proxy: str = "") -> Dict:
        """
        获取登录二维码(绕过验证码)
        Args:
            key: 账号唯一标识
            check: 修改代理时(SetProxy接口) 是否发送检测代理请求(可能导致请求超时)
            proxy: socks代理，例如：socks5://username:password@ipv4:port
        Returns:
            Dict: 包含二维码信息的字典
        """
        url = f"{self.base_url}/login/GetLoginQrCodeNewX"
        json_data = {
            "Check": check,
            "Proxy": proxy
        }
        return post_json(base_url=url, token=key, data=json_data)

    def login_new(self, key: str, device_info: Dict, login_data: str, password: str, proxy: str = "", ticket: str = "", type: int = 0, username: str = "") -> Dict:
        """
        62LoginNew新疆号登录
        Args:
            key: 账号唯一标识
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
        url = f"{self.base_url}/login/LoginNew"
        json_data = {
            "DeviceInfo": device_info,
            "LoginData": login_data,
            "Password": password,
            "Proxy": proxy,
            "Ticket": ticket,
            "Type": type,
            "UserName": username
        }
        return post_json(base_url=url, token=key, data=json_data)

    def phone_device_login(self, key: str, url: str = "") -> Dict:
        """
        辅助新手机登录
        Args:
            key: 账号唯一标识
            url: URL
        Returns:
            Dict: 辅助新手机登录操作的结果
        """
        api_url = f"{self.base_url}/login/PhoneDeviceLogin"
        json_data = {
            "Url": url
        }
        return post_json(base_url=api_url, token=key, data=json_data)
