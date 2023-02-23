import re
import time

import requests




def return_png(times):
    for _ in range(times):
        r = requests.get('https://cataas.com/cat')
        with open(f'cat{_}.png', 'wb') as f:
            f.write(r.content)


# return_png(2)

def return_server_from_url(*args):
    print(f"{'URL':<22}{'Server':<15}")
    print("-" * 100)
    for i in args:
        r = requests.get(i)
        print(f"{i:<20} - {r.headers['Server']:<15}")


delfi = 'http://delfi.lt'
min15 = 'http://15min.lt'
skelbiult = 'http://skelbiu.lt'
# return_server_from_url('https://pagalba.ignitis.lt/8673637288290/?k=93747963')
# return_server_from_url(delfi, skelbiult, min15)


def return_weather(city):
    pattern = re.compile(r"<b>Šiuo metu: </b>\n.*\n.*[0-9]°")
    pattern2 = re.compile(r'[0-9]+°')
    r = requests.get(f'https://orai.15min.lt/prognoze/{city}')
    temp = str(r.text)
    tempr = pattern.findall(temp)
    a = str(tempr)
    temperature = pattern2.findall(a)
    print(f'It is now {temperature[0]} degrees in {city.capitalize()}')

return_weather("kaunas")
