import requests
from pprint import pprint

# jojo reference lol


api_key = 'you can get it on https://openweathermap.org/'
url = 'http://api.openweathermap.org/data/2.5/weather'
icon_url = 'http://openweathermap.org/img/wn/13d@2x.png'
img_size_x2 = '@2x'
img_size = ''

def get_weather_data(city):
	base_url = f'{url}?appid={api_key}&q={city}'
	raw_wd = requests.get(base_url).json()

	if raw_wd['cod'] == 200:
		return  { 
			"country": raw_wd['sys']['country'],
			"city": raw_wd['name'],
			"feels_like": round(raw_wd['main']['feels_like']-273.15),
			"temp": round(raw_wd['main']['temp']-273.15),
			"main": raw_wd['weather'][0]['main'],
			"description": raw_wd['weather'][0]['description'],
			"icon": f"http://openweathermap.org/img/wn/{raw_wd['weather'][0]['icon']}{img_size_x2}.png"
		}
	else:
		return False

pprint(get_weather_data('moscow'))