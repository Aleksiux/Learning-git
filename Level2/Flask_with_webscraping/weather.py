import re
import requests


def return_weather(city):
    pattern = re.compile(r"<b>Šiuo metu: </b>\n.*\n.*[0-9]°")
    pattern2 = re.compile(r'[0-9]+°|-[0-9]+°')
    r = requests.get(f'https://orai.15min.lt/prognoze/{city}')
    temp = str(r.text)
    tempr = pattern.findall(temp)
    a = str(tempr)
    temperature = pattern2.findall(a)
    return f'In {city.capitalize()} {temperature[0]}'



