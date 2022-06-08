import tkinter as tk
import requests
import time

import datetime

#get Weather data from API 
def get_weather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=24a3989fe59d302b367dc05598ad6332"
    json_data = requests.get(api).json()
    
    #gets current condition
    condition = json_data['weather'][0]['main']
   
    #converts temperature from Kelvin to Celsius
    temp = int(json_data['main']['temp'] - 273.15)

    #gets min and max temp
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)

    #gets humidiy data
    humidity = json_data['main']['humidity']

    #gets wind speed
    wind = json_data['wind']['speed']

    #access sunrise and sunset time in seconds, converts to 12hour
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 14400))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 14400))

    #stores weather conditions  
    output_temp = condition + "\n" + str(temp) + "°C"
    output_data = "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

    #text for printing output
    label1.config(text=output_temp)
    label2.config(text=output_data)

#set Canvas size
canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("Weather App")

f = ("poppins", 16, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas,font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', get_weather)

#creates Labels
label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()
