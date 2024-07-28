import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = 'your_api_key_here'
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    
    if data['cod'] == 200:
        main = data['main']
        weather = data['weather'][0]
        result = f"City: {data['name']}\nTemperature: {main['temp']}°C\nHumidity: {main['humidity']}%\nCondition: {weather['description']}"
        weather_label.config(text=result)
    else:
        messagebox.showerror("Error", "City not found!")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place the widgets
city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="", font=("Helvetica", 14))
weather_label.pack()

# Run the application
root.mainloop()
