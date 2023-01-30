import json
import csv
import requests

ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174',
           '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']

key_ip = 'BD9wolml7hpKG7eXE9TnjQV1FWJWWIkTFJhS3Zrz'
key_weather = 'bd3b94b3f971d1f5138d6fc24342aba5'
url_ip = "https://api.ipbase.com/v2/info"
url_weather = 'https://api.openweathermap.org/data/2.5/weather'
fieldname = ['IP', 'City', 'Country', 'Temp', 'Weather']

with open('weather.csv', 'a', encoding='UTF8', newline='') as f:
    obj = csv.DictWriter(f, fieldnames=fieldname)
    obj.writeheader()

for ip in ip_list:
    """
    PART 1 GET lat,long,city
    """
    params_ip = {
        'ip': ip,
        'apikey': key_ip
    }
    resp_ip = requests.get(url_ip, params=params_ip)
    data_ip = json.loads(resp_ip.text)
    lat = data_ip['data']['location']['latitude']
    long = data_ip['data']['location']['longitude']
    city = data_ip['data']['location']['city']['name']
    country = data_ip['data']['location']['country']['name']
    """
    PART 2 GET TEMP/WEATHER
    """
    params_weather = {
        'lat': lat,
        'lon': long,
        'units': 'metric',
        'appid': key_weather,
    }
    resp_weather = requests.post(url_weather, params=params_weather)
    data_weather = json.loads(resp_weather.text)
    weather = data_weather['weather'][0]['main']
    temp = data_weather['main']['temp']
    main_data = [
        {'IP': ip,
         'City': city,
         'Country': country,
         'Temp': temp,
         'Weather': weather}
    ]
    with open('weather.csv', 'a', encoding='UTF8', newline='') as f:
        obj = csv.DictWriter(f, fieldname)
        obj.writerow(main_data[0])
