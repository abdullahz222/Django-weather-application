import json
import requests

def info_by_countryCode_and_cityName(cityName,countryCode):
	url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&appid=39ea0cb4820b6f21571039fb5e5b3bce".format(cityName,countryCode)
	r = requests.get(url)
	ans= r.json()
	return ans
	# print(ans['weather'][0]['description'])
def formatted_info(cityName,countryCode):
	info_set= info_by_countryCode_and_cityName(cityName,countryCode)
	info_list=[]

	for item in info_set:
 		info_list.append(info_set[item])

	for info in info_list:
		if type(info)==dict:		
			for i in info:
				print(i +' = '+ str(info[i]), end="\n\n")

		elif type(info)==list:
			info_list = (info[0])
			for inf in info_list:
				print(inf +' = '+ str(info_list[inf]),end="\n\n")
		
		else:		
			print(i +' = '+ str(info),end="\n\n")

#use this like formatted_info('lahore','586')

def formatted_info2(info_set):
	
	info_list=[]

	for item in info_set:
		info_list.append(info_set[item])

	for info in info_list:

		if type(info)==dict:	

			for i in info:
				print(i +' = '+ str(info[i]), end="\n\n")

		elif type(info)==list:
			info_list = (info[0])
			for inf in info_list:
				print(inf +' = '+ str(info_list[inf]),end="\n\n")
		
		# elif type(info)==str:		
		# 	print(str(item)+' = ',end="\n\n")

		# else:
		# 	print("this is integer"+str(info))


formatted_info2(info_by_countryCode_and_cityName("bahawalpur","586"))
## you can use any function inside formateed info2 as long as it returns a dataset

