import requests
import current
import pytemperature
import time


def get_info(request):
    data = []
    city = request['city']['name']

    for day in request['list']:
        convert = time.localtime(day['dt'])
        date = str(convert.tm_mday) + '.' + str(convert.tm_mon)
        desc = day['weather'][0]['description']
        temp_day = int(day['temp']['day'])
        temp_night = int(day['temp']['night'])
        humidity = str(day['humidity']) + '%'

        data.append({
            'Город:': city,
            'Дата:': date,
            'Температура:': {'в день:': str(temp_day) + '°C', 'в ноч:': str(temp_night) + '°C'},
            'Влажность:': humidity,
            'Описание:': str(desc),
        })
    return data


if __name__ == "__main__":
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = input('Введите город: ')
    days = input('Введите количество дней: ')
    request = current.parse(url, city, days)
    data = get_info(request)
    for_city = '------------------------------------------- ' + \
        city + ' ----------------------------------------'
    print(for_city)
    for day in data:
        date = day['Дата:']
        for_day = '------------------------------------------ ' + \
            date + ' ----------------------------------------'
        print(for_day)
        print('Температура: ' + 'в день: ' + day['Температура:']['в день:'] + ' в ноч: ' + day['Температура:']['в ноч:'])
        print('Влажность:', day['Влажность:'])
        print('Описание:', day['Описание:'])
