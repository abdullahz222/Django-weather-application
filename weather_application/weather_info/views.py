from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .api_check import info_by_cityName_and_countryName
from .db import list_country_only
import datetime 

def Landing_page(request):
	return render(request,'weather_info/index.html')

def Services(request):
	if request.method=='POST':
		submitbutton= request.POST.get("submit")
		form= UserForm(request.POST or None)
		if form.is_valid():

			Country_name= form.cleaned_data.get("fname")
			City_name= form.cleaned_data.get("lname")

			ans = info_by_cityName_and_countryName(City_name,Country_name)
			if ans['cod']==200:
				print(ans)
				longitude= ans['coord']['lon']
				latitude= ans['coord']['lat']
				weather_condition = ans['weather'][0]['main']
				weather_condition_des = ans['weather'][0]['description']
				temperature = ans['main']['temp']
				minimum_temperature = ans['main']['temp_min']
				maximum_temperature = ans['main']['temp_max']
				pressure = ans['main']['pressure']
				humidity = ans['main']['humidity']
				visibility= ans['visibility']
				wind_speed = ans['wind']['speed']
				wind_direction=ans['wind']['deg']
				time_of_calculation = datetime.datetime.fromtimestamp(ans['dt'])
				sunrise = datetime.datetime.fromtimestamp(ans['sys']['sunrise'])
				sunset = datetime.datetime.fromtimestamp(ans['sys']['sunset'])
				timezone =  datetime.datetime.fromtimestamp(ans['timezone'])
				name = ans['name']
				found = True

				
				
				context = {'longitude':longitude,
							'latitude':latitude,
							'weather_condition':weather_condition,
							'weather_condition_des':weather_condition_des,
							'temperature':temperature,
							'minimum_temperature':minimum_temperature,
							'maximum_temperature':maximum_temperature,
							'pressure':pressure,
							'humidity':humidity,
							'visibility':visibility,
							'wind_speed':wind_speed,
							'wind_direction':wind_direction,
							'time_of_calculation':time_of_calculation,
							'sunrise':sunrise,
							'sunset':sunset,
							'timezone':timezone,
							'name':name,
							'found':found
							}

				return render(request,'weather_info/services.html',context)	
			else:
				notfound = True
				return render(request, 'weather_info/services.html', {"notfound":notfound})	

	countries_list = list_country_only()
	context={'countries_list':countries_list}

	return render(request,'weather_info/services.html', context)

def About(request):
	return render(request,'weather_info/about.html')

def Contact(request):
	if request.method=='POST':
		print(request.POST)
	return render(request,'weather_info/contact.html')
# Create your views here.


