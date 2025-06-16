from typing import Dict, List, Optional
from libs.wechatpad_api.util.http_util import post_json, get_json


class OfficialAccountApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化OfficialAccountApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def auth_mp_login(self, key: str, opcode: int, scene: int, url: str) -> Dict:
        """
        授权公众号登录
        Args:
            key: 账号唯一标识
            opcode: 操作码
            scene: 场景
            url: URL
        Returns:
            Dict: 授权公众号登录操作的结果
        """
        api_url = f"{self.base_url}/applet/AuthMpLogin"
        json_data = {
            "Opcode": opcode,
            "Scene": scene,
            "Url": url
        }
        return post_json(base_url=api_url, token=key, data=json_data)

    def follow_gh(self, key: str, gh_list: List[Dict]) -> Dict:
        """
        关注公众号
        Args:
            key: 账号唯一标识
            gh_list: 公众号列表，每个元素为包含 "Gh", "Scene" 的字典
        Returns:
            Dict: 关注公众号操作的结果
        """
        url = f"{self.base_url}/applet/FollowGH"
        json_data = {"GHList": gh_list}
        return post_json(base_url=url, token=key, data=json_data)

    def get_a8_key(self, key: str, opcode: int, req_url: str, scene: int) -> Dict:
        """
        授权链接 (GetA8Key)
        Args:
            key: 账号唯一标识
            opcode: 操作码
            req_url: 请求URL
            scene: 场景
        Returns:
            Dict: 授权链接操作的结果
        """
        url = f"{self.base_url}/applet/GetA8Key"
        json_data = {
            "OpCode": opcode,
            "ReqUrl": req_url,
            "Scene": scene
        }
        return post_json(base_url=url, token=key, data=json_data)

    def get_mp_a8_key(self, key: str, opcode: int, scene: int, url: str) -> Dict:
        """
        授权链接 (GetMpA8Key)
        Args:
            key: 账号唯一标识
            opcode: 操作码
            scene: 场景
            url: URL
        Returns:
            Dict: 授权链接操作的结果
        """
        api_url = f"{self.base_url}/applet/GetMpA8Key"
        json_data = {
            "Opcode": opcode,
            "Scene": scene,
            "Url": url
        }
        return post_json(base_url=api_url, token=key, data=json_data)

    def get_mp_history_message(self, key: str, url: str) -> Dict:
        """
        获取公众号历史消息
        Args:
            key: 账号唯一标识
            url: URL
        Returns:
            Dict: 公众号历史消息列表
        """
        api_url = f"{self.base_url}/applet/GetMpHistoryMessage"
        json_data = {"Url": url}
        return post_json(base_url=api_url, token=key, data=json_data)

    def js_operate_wx_data(self, key: str, app_id: str, data: str = "", opt: int = 1, package_name: str = "", sdk_name: str = "") -> Dict:
        """
        小程序云函数操作
        Args:
            key: 账号唯一标识
            app_id: 应用ID
            data: 小程序云函数操作的 Data; json字符串, 注意必须是 json 字符串; 传空时默认值为: '{"with_credentials":true,"from_component":true,"data":{"lang":"zh_CN"},"api_name":"webapi_getuserinfo"}'
            opt: 小程序云函数操作的 Opt; 默认为1
            package_name: PackageName
            sdk_name: SdkName
        Returns:
            Dict: 小程序云函数操作的结果
        """
        url = f"{self.base_url}/applet/JSOperateWxData"
        json_data = {
            "AppId": app_id,
            "Data": data,
            "Opt": opt,
            "PackageName": package_name,
            "SdkName": sdk_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def js_login(self, key: str, app_id: str, data: str = "", opt: int = 1, package_name: str = "", sdk_name: str = "") -> Dict:
        """
        授权小程序(返回授权后的code)
        Args:
            key: 账号唯一标识
            app_id: 应用ID
            data: 小程序云函数操作的 Data
            opt: 小程序云函数操作的 Opt
            package_name: PackageName
            sdk_name: SdkName
        Returns:
            Dict: 授权小程序操作的结果
        """
        url = f"{self.base_url}/applet/JsLogin"
        json_data = {
            "AppId": app_id,
            "Data": data,
            "Opt": opt,
            "PackageName": package_name,
            "SdkName": sdk_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def qr_connect_authorize(self, key: str, qr_url: str) -> Dict:
        """
        二维码授权请求
        Args:
            key: 账号唯一标识
            qr_url: 二维码URL
        Returns:
            Dict: 二维码授权请求操作的结果
        """
        api_url = f"{self.base_url}/applet/QRConnectAuthorize"
        json_data = {"QrUrl": qr_url}
        return post_json(base_url=api_url, token=key, data=json_data)

    def qr_connect_authorize_confirm(self, key: str, qr_url: str) -> Dict:
        """
        二维码授权确认
        Args:
            key: 账号唯一标识
            qr_url: 二维码URL
        Returns:
            Dict: 二维码授权确认操作的结果
        """
        api_url = f"{self.base_url}/applet/QRConnectAuthorizeConfirm"
        json_data = {"QrUrl": qr_url}
        return post_json(base_url=api_url, token=key, data=json_data)

    def sdk_oauth_authorize(self, key: str, app_id: str, data: str = "", opt: int = 1, package_name: str = "", sdk_name: str = "") -> Dict:
        """
        应用授权
        Args:
            key: 账号唯一标识
            app_id: 应用ID
            data: 数据
            opt: Opt
            package_name: PackageName
            sdk_name: SdkName
        Returns:
            Dict: 应用授权操作的结果
        """
        url = f"{self.base_url}/applet/SdkOauthAuthorize"
        json_data = {
            "AppId": app_id,
            "Data": data,
            "Opt": opt,
            "PackageName": package_name,
            "SdkName": sdk_name
        }
        return post_json(base_url=url, token=key, data=json_data)