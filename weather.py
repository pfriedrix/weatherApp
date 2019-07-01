import requests
import pytemperature
import time


url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
city = input('Введите город: ')


def parse(url, city):
	request = requests.get(url.format(city)).json()
	return request


def convert_time(s):
	now = time.localtime(s)
	return str(now.tm_hour) + ':' + str(now.tm_min)


def get_info(request):
	city = request['name']
	temp = pytemperature.f2c(request['main']['temp'])
	desc = request['weather'][0]['description']
	humdity = request['main']['humidity']
	clouds = request['clouds']['all']
	sunrise = convert_time(request['sys']['sunrise'])
	sunset = convert_time(request['sys']['sunset'])

	weather = {
		'Город:': city,
		'Температура:': str(temp) + '°C',
		'Описание:': desc,
		'Влажность:': str(humdity) + '%',
		'Вероятность осадков:': str(clouds) + '%',
		'Восход:': sunrise,
		'Закат:': sunset,
	}
	return weather

weather = get_info(parse(url, city))


for key, value in weather.items():
	print(key, value)