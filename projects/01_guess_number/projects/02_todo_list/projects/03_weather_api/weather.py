import requests

API_KEY = "your_api_key_here"  # replace with your OpenWeatherMap key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + f"appid={API_KEY}&q={city}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        temp = main["temp"]
        humidity = main["humidity"]
        weather = data["weather"][0]["description"]
        print(f"🌍 City: {city}")
        print(f"🌡 Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"⛅ Weather: {weather}")
    else:
        print("City not found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
