import requests
import tkinter as tk

def get_weather():
    city = city_entry.get()
    API_key = "USE_YOUR_OWN_API_KEY" # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temp_label.config(text=f"Temperature: {data['main']['temp']}°C")
        weather_label.config(text=f"Weather: {data['weather'][0]['description']}")
        humidity_label.config(text=f"Humidity: {data['main']['humidity']}%")
        wind_label.config(text=f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        temp_label.config(text="City not found.")
        weather_label.config(text="")
        humidity_label.config(text="")
        wind_label.config(text="")

root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=5)

temp_label = tk.Label(root, text="", font=("Arial", 12))
temp_label.pack()

weather_label = tk.Label(root, text="", font=("Arial", 12))
weather_label.pack()

humidity_label = tk.Label(root, text="", font=("Arial", 12))
humidity_label.pack()

wind_label = tk.Label(root, text="", font=("Arial", 12))
wind_label.pack()

root.mainloop()



