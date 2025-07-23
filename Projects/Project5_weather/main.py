import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    """Fetches the current weather for the specified city."""
    city = entry_city.get()
    api_key = 'YOUR_API_KEY'  # Replace with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city_name = data['name']
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            message = f"Weather in {city_name}:\nTemperature: {temperature}°C\nDescription: {weather_description.capitalize()}"
            messagebox.showinfo("Weather Report", message)
        else:
            messagebox.showerror("Error", data["message"])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Create and place widgets
label = tk.Label(root, text="Enter City Name:", bg="#f0f0f0", font=("Helvetica", 12))
label.pack(pady=10)

entry_city = tk.Entry(root, width=30, font=("Helvetica", 12))
entry_city.pack(pady=5)

button = tk.Button(root, text="Get Weather", command=get_weather, bg="#4CAF50", fg="white", font=("Helvetica", 12))
button.pack(pady=20)

# Start the main event loop
root.mainloop()