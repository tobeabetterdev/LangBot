import json
import requests

def get_weather():
    api_url = "https://cn.apihz.cn/api/tianqi/tqyb.php?id=10004000&key=3418000b09d44d3a3eb5e69cabe044e7&sheng=浙江省&place=滨江区"  # API 地址

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            text = response.text
            return json.loads(text)
        else:
            print(f"获取天气信息失败，状态码：{response.status_code}")
            return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

def compose_weather_message(weather_json):
    place = weather_json['place']
    temperature = weather_json['temperature']
    weather1 = weather_json['weather1']
    weather2 = weather_json['weather2']
    precipitation = weather_json['precipitation']
    windDirection = weather_json['windDirection']
    windDirectionDegree = weather_json['windDirectionDegree']
    windSpeed = weather_json['windSpeed']
    windScale = weather_json['windScale']
    humidity = weather_json['humidity']
    pressure = weather_json['pressure']
    message = (
        f"--- {place} 实时天气☁️ ---\n"
        f"🌡️当前温度：{temperature}℃\n"
        f"🌡️气压{pressure}㍱\n"
        f"☁️天气：{weather1}转{weather2}\n"
        f"💨风向：{windDirection}\n"
        f"💨风向角度：{windDirectionDegree}°\n"
        f"🌬️风速：{windSpeed}\n"
        f"🌬️风力等级：{windScale}级\n"
        f"💦湿度：{humidity}%\n"
        f"🌧️降水量：{precipitation}mm/h"
    )

    return message

def main():
    good_morning = '核桃妈妈早上好，记得吃早餐、喝叶酸、喝维生素D2，出门记得带车钥匙哟~\n'
    weather_info = get_weather()  # 获取天气信息
    if weather_info and weather_info['code'] == 200:
        good_morning += compose_weather_message(weather_info)

    print(good_morning)  # 打印 Markdown 内容


if __name__ == "__main__":
    main()