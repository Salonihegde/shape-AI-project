import requests
#import os
from datetime import datetime


def main():
    outfile = open('data.txt','w')
    api_key = 'a79e9615a12d86939cc81fe812095f34'
    location = input("Enter the city name: ")

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-------------------------------------------------------------")
    print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print("-------------------------------------------------------------")

    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current weather desc  :", weather_desc)
    print("Current Humidity      :", hmdt, '%')
    print("Current wind speed    :", wind_spd, 'kmph')

    outfile.write('Location = ' + location.upper() + '\n')
    outfile.write('Current Temperature = ' + str(temp_city) + ' deg C' + '\n')
    outfile.write('Current Weather = ' + weather_desc + '\n')
    outfile.write('Current Humidity = ' + str(hmdt) + '%' + '\n')
    outfile.write('Current Wind Speed = ' + str(wind_spd) +' kmph' + '\n')
    outfile.write(date_time)

    outfile.close()

main()



