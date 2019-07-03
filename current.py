import requests
import pytemperature
import time
import datetime



def parse(url, *args):
    request = requests.get(url.format(*args)).json()
    return request


def convert_time(s):
    now = time.localtime(s)
    return str(now.tm_hour) + ':' + str(now.tm_min)


def get_info(request):
    city = request['name']
    temp = int(request['main']['temp'])
    desc = request['weather'][0]['description']
    humdity = request['main']['humidity']
    sunrise = convert_time(request['sys']['sunrise'])
    sunset = convert_time(request['sys']['sunset'])

    weather = {
        'Город:': city,
        'Дата:': datetime.datetime.today().strftime('%d.%m.%Y'),
        'Температура:': str(temp) + '°C',
        'Описание:': desc,
        'Влажность:': str(humdity) + '%',
        'Восход:': sunrise,
        'Закат:': sunset,
    }
    return weather


if __name__ == "__main__":
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = input('Введите город: ')
    weather = get_info(parse(url, city))
    for key, value in weather.items():
    	print(key, value)
