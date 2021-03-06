# -*- coding: utf-8 -*-
"""weather.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FykCbNp_gxkEWKiNV2mni7im335C6uDx
"""

import requests

from datetime import datetime
api_key = "923a90cd05983fccb77cf6b53297f84b"
location = input("Enter the city name:")
 
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city =((api_data['main']['temp'])-273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y| %I %M %S %p")

f=open("\n weatherapi.txt",'w')
f.write("\n -------------------------------------------------------------------")
f.write("\n Weather Stats for - {} || {}".format(location.upper(),date_time))
f.write("\n -------------------------------------------------------------------")

f.write("\n Current Temperature is : {:.2f} deg C".format(temp_city))
f.write("\n Current Weather desc  : {}".format(weather_desc))
f.write("\n Current Humidity       : {} %".format(hmdt))
f.write("\n Current wind speed     : {} kmph".format(wind_spd))
f.close()