from typing import Dict, Optional
from libs.wechatpad_api.util.http_util import get_json, post_json


class PayApi:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化PayApi
        Args:
            base_url: API的基础URL
            token: 用户的认证token
        """
        self.base_url = base_url
        self.token = token

    def collect_money(self, key: str, invalid_time: str, to_user_name: str, transfer_id: str, transaction_id: str) -> Dict:
        """
        确定收款
        Args:
            key: 账号唯一标识
            invalid_time: 无效时间
            to_user_name: 接收者wxid
            transfer_id: 转账ID
            transaction_id: 交易ID
        Returns:
            Dict: 确定收款操作的结果
        """
        url = f"{self.base_url}/pay/Collectmoney"
        json_data = {
            "InvalidTime": invalid_time,
            "ToUserName": to_user_name,
            "TransFerId": transfer_id,
            "TransactionId": transaction_id
        }
        return post_json(base_url=url, token=key, data=json_data)

    def confirm_pre_transfer(self, key: str, bank_serial: str, bank_type: str, pay_password: str, req_key: str) -> Dict:
        """
        确认转账(客户端版本过低会无法转账)
        Args:
            key: 账号唯一标识
            bank_serial: 付款方式 Serial序列号
            bank_type: 付款方式 类型
            pay_password: 支付密码
            req_key: 创建转账返回的ReqKey
        Returns:
            Dict: 确认转账操作的结果
        """
        url = f"{self.base_url}/pay/ConfirmPreTransfer"
        json_data = {
            "BankSerial": bank_serial,
            "BankType": bank_type,
            "PayPassword": pay_password,
            "ReqKey": req_key
        }
        return post_json(base_url=url, token=key, data=json_data)

    def create_pre_transfer(self, key: str, description: str, fee: int, to_user_name: str) -> Dict:
        """
        创建转账
        Args:
            key: 账号唯一标识
            description: 转账备注
            fee: 转账金额(单位为分)
            to_user_name: 要转账用户的wxid
        Returns:
            Dict: 创建转账操作的结果
        """
        url = f"{self.base_url}/pay/CreatePreTransfer"
        json_data = {
            "Description": description,
            "Fee": fee,
            "ToUserName": to_user_name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def generate_pay_qrcode(self, key: str, money: str, name: str) -> Dict:
        """
        生成自定义收款二维码
        Args:
            key: 账号唯一标识
            money: 金额(单位为分), 999 即为 9.99 元
            name: 收款备注
        Returns:
            Dict: 生成收款二维码操作的结果
        """
        url = f"{self.base_url}/pay/GeneratePayQCode"
        json_data = {
            "Money": money,
            "Name": name
        }
        return post_json(base_url=url, token=key, data=json_data)

    def get_band_card_list(self, key: str) -> Dict:
        """
        获取银行卡信息
        Args:
            key: 账号唯一标识
        Returns:
            Dict: 银行卡信息列表
        """
        url = f"{self.base_url}/pay/GetBandCardList"
        return post_json(base_url=url, token=key)

    def get_red_envelopes_detail(self, key: str, hong_bao_item: Dict) -> Dict:
        """
        查看红包详情
        Args:
            key: 账号唯一标识
            hong_bao_item: 红包项，包含 NativeURL 等信息
        Returns:
            Dict: 红包详情
        """
        url = f"{self.base_url}/pay/GetRedEnvelopesDetail"
        json_data = {"HongBaoItem": hong_bao_item}
        return post_json(base_url=url, token=key, data=json_data)

    def get_red_packet_list(self, key: str, hong_bao_item: Dict, limit: int, native_url: str, offset: int) -> Dict:
        """
        查看红包领取列表
        Args:
            key: 账号唯一标识
            hong_bao_item: 红包项，包含 ChannelID, MsgType, SendID, SendUserName, ShowSourceMac, ShowWxPayTitle, Sign, Ver
            limit: 限制数量
            native_url: 原生URL
            offset: 偏移量
        Returns:
            Dict: 红包领取列表
        """
        url = f"{self.base_url}/pay/GetRedPacketList"
        json_data = {
            "HongBaoItem": hong_bao_item,
            "Limit": limit,
            "NativeURL": native_url,
            "Offset": offset
        }
        return post_json(base_url=url, token=key, data=json_data)

    def open_red_envelopes(self, key: str, native_url: str) -> Dict:
        """
        拆红包
        Args:
            key: 账号唯一标识
            native_url: 红包的NativeURL
        Returns:
            Dict: 拆红包操作的结果
        """
        url = f"{self.base_url}/pay/OpenRedEnvelopes"
        json_data = {"NativeUrl": native_url}
        return post_json(base_url=url, token=key, data=json_data)

    def wx_create_red_packet(self, key: str, amount: int, content: str, count: int, _from: int, red_type: int, username: str) -> Dict:
        """
        创建红包
        Args:
            key: 账号唯一标识
            amount: 每个红包的金额(单位为分, 最小为100); 总金额为 Amount*Count
            content: 红包的备注内容(祝福语)
            count: 红包个数(最少为1)
            _from: InAway(0:群红包; 1:个人红包)
            red_type: 红包类型(0 普通红包; 1 拼手气红包; ? 专属红包)
            username: 红包接收者; wxid 或 群ID
        Returns:
            Dict: 创建红包操作的结果
        """
        url = f"{self.base_url}/pay/WXCreateRedPacket"
        json_data = {
            "Amount": amount,
            "Content": content,
            "Count": count,
            "From": _from,
            "RedType": red_type,
            "Username": username
        }
        return post_json(base_url=url, token=key, data=json_data)