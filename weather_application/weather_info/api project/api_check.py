import json
import requests
from access_data import *
##api key
api_key = "39ea0cb4820b6f21571039fb5e5b3bce"

def info_by_zip(zipcode,country_abbr):
	url = "http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid=39ea0cb4820b6f21571039fb5e5b3bce".format(zipcode,country_abbr)
	r = requests.get(url)
	ans = r.json()
	print(ans['weather'][0]['description'])
## use this function like info_by_zip(63100,"pk")


def info_by_countryCode_and_cityName(cityName,countryCode):
	url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&appid=39ea0cb4820b6f21571039fb5e5b3bce".format(cityName,countryCode)
	r = requests.get(url)
	ans= r.json()
	print(ans)
	print(ans['weather'][0]['description'])

# use this function like info_by_countryCode_and_cityName("bahawalpur","586")


def info_by_cityName_and_countryName(cityName,countryName):
	countryCode = convertor(countryName)
	url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&appid=39ea0cb4820b6f21571039fb5e5b3bce".format(cityName,countryCode)
	r = requests.get(url)
	ans= r.json()
	print(ans)

info_by_cityName_and_countryName("lahore","Pakistan")



