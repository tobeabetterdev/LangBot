import requests

from typing import Optional, Dict
import requests
import aiohttp
import asyncio


def post_json(base_url: str, token: Optional[str] = None, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
    headers = {
        'Content-Type': 'application/json'
    }
    if token:
        if params is None:
            params = {}
        params['key'] = token

    try:
        response = requests.post(base_url, json=data, headers=headers, params=params, timeout=60)
        response.raise_for_status()
        result = response.json()

        if result:
            return result
        else:
            raise RuntimeError(response.text)
    except Exception as e:
        print(f"http请求失败, url={base_url}, exception={e}")
        raise RuntimeError(str(e))

def get_json(base_url: str, token: Optional[str] = None, params: Optional[Dict] = None) -> Dict:
    headers = {
        'Content-Type': 'application/json'
    }
    if token:
        if params is None:
            params = {}
        params['key'] = token

    try:
        response = requests.get(base_url, headers=headers, params=params, timeout=60)
        response.raise_for_status()
        result = response.json()

        if result:
            return result
        else:
            raise RuntimeError(response.text)
    except Exception as e:
        print(f"http请求失败, url={base_url}, exception={e}")
        raise RuntimeError(str(e))


async def async_request(
        base_url: str,
        token_key: str,
        method: str = 'POST',
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None
):
    """
    通用异步请求函数

    :param base_url: 请求URL
    :param token_key: 请求token (将作为'key'查询参数)
    :param method: HTTP方法 (GET, POST, PUT, DELETE等)
    :param params: URL查询参数
    :param data: 表单数据
    :param json: JSON数据
    :return: 响应文本
    """
    headers = {
        'Content-Type': 'application/json'
    }
    
    if params is None:
        params = {}
    params['key'] = token_key # 将token_key作为'key'查询参数

    async with aiohttp.ClientSession() as session:
        async with session.request(
                method=method,
                url=base_url, # 不再手动拼接url，而是通过params传递
                params=params,
                headers=headers,
                data=data,
                json=json
        ) as response:
            response.raise_for_status()  # 如果状态码不是200，抛出异常
            result = await response.json()
            return result

