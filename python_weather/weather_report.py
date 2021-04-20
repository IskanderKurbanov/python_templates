import requests
from pprint import pprint

# jojo reference lol


api_key = 'you can get it on https://openweathermap.org/'


print(__name__)

#  OpenWeather
api_key = 'you can get it on https://openweathermap.org/'
url = 'http://api.openweathermap.org/data/2.5/weather'
icon_url = 'http://openweathermap.org/img/wn/13d@2x.png'
img_size_x2 = '@2x'
img_size = ''

# TimeZoneDB
api_key_time = 'you can get it on https://timezonedb.com/'
url_time = 'http://api.timezonedb.com/v2.1/get-time-zone'
data_format = 'json'
time_by = 'position'


def get_weather_data(city):
	base_url = f'{url}?appid={api_key}&q={city}'
	raw_weather_data = requests.get(base_url).json()

	if raw_weather_data['cod'] == 200:
		return  { 
			"country": raw_weather_data['sys']['country'],
			"city": raw_weather_data['name'],
			"feels_like": round(raw_weather_data['main']['feels_like']-273.15),
			"temp": round(raw_weather_data['main']['temp']-273.15),
			"main": raw_weather_data['weather'][0]['main'],
			"description": raw_weather_data['weather'][0]['description'],
			"icon": f"http://openweathermap.org/img/wn/{raw_weather_data['weather'][0]['icon']}{img_size_x2}.png"
		}
	else:
		return False


def get_weather_data_with_time(city):
	base_url = f'{url}?appid={api_key}&q={city}'
	raw_weather_data = requests.get(base_url).json()

	if raw_weather_data['cod'] == 200:
		lat = raw_weather_data['coord']['lat']
		lng = raw_weather_data['coord']['lon']
		time_url = f'{url_time}?key={api_key_time}&format={data_format}&by={time_by}&lat={lat}&lng={lng}'
		raw_time_data = requests.get(time_url).json()

		if raw_time_data['status'] == 'OK':

			return  { 
				"country": raw_weather_data['sys']['country'],
				"city": raw_weather_data['name'],
				"weather": {
					"feels_like": round(raw_weather_data['main']['feels_like']-273.15),
					"temp": round(raw_weather_data['main']['temp']-273.15),
					"main": raw_weather_data['weather'][0]['main'],
					"description": raw_weather_data['weather'][0]['description'],
					"icon": f"http://openweathermap.org/img/wn/{raw_weather_data['weather'][0]['icon']}{img_size_x2}.png",
				},
				"time": raw_time_data['formatted']
			}
		else:
			return get_weather_data(city)
	else:
		return False


pprint(get_weather_data('moscow'))
pprint(get_weather_data_with_time('moscow'))
