import datetime
import time
import urllib

import peewee
import pytemperature
import requests
from setuptools import Command

from models import *


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


def is_connected():
    req = urllib.request.Request('https://google.com')
    try:
        urllib.request.urlopen(req)
        return True
    except urllib.error.URLError as err:
        print('Bad Connection')
        return False


def send_to_db(data):
    exist = False
    try:
        Weather.select().where(
            Weather.city == data['Город:'] and Weather.date == data['Дата:']).get()
    except DoesNotExist:
        exist = True
    if exist:
        row = Weather(
            city=data['Город:'],
            date=data['Дата:'],
            temp=data['Температура:'],
            desc=data['Описание:'],
            humdity=data['Влажность:'],
            sunrise=data['Восход:'],
            sunset=data['Закат:'],
        )
        row.save()


if __name__ == "__main__":
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = input('Введите город: ')
    if is_connected():
        request = parse(url, city)
        weather = get_info(request)
        send_to_db(weather)
        for key, value in weather.items():
            print(key, value)
