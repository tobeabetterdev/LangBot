import requests

def get_morning_news():
    api_urls = [
        "https://api.suxun.site/api/sixs",  # 主API
        "https://api.03c3.cn/api/zb",       # 备API
    ]
    
    for url in api_urls:
        try:
            response = requests.get(url, timeout=5)  # 添加超时参数
            if response.status_code == 200:
                return response.url # 获取最终图片URL
            else:
                print(f"API {url} 访问失败，状态码：{response.status_code}")
        except Exception as e:
            pass

    return None

def main():
    image_url = get_morning_news()  # 获取图片 URL
    if image_url and image_url.startswith("http"):
        markdown_image_link = f"![Morning News Image]({image_url})"  # 转换为 Markdown 格式
        print(markdown_image_link)  # 打印 Markdown 图片链接
    else:
        print("无法获取图片或图片链接无效")  # 打印错误信息

if __name__ == "__main__":
    main()