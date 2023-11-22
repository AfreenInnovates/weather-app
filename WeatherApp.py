import requests
import pyttsx3
engine = pyttsx3.init()
url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "6e366941f1388d834e8a673f26cf8549"
print("Welcome!")
city = input("Enter a city name: ")

query_url = f"{url}q={city}&appid={api_key}&units=imperial"

response = requests.get(query_url)
weather_data = response.json()

if response.status_code == 200:
    weather = f"\nCurrent weather in {weather_data['name']}, {weather_data['sys']['country']}:\n"
    temp = f"Temperature: {weather_data['main']['temp']} F"
    feelslike = f"Feels like: {weather_data['main']['feels_like']} F"
    humidity = f"Humidity: {weather_data['main']['humidity']}%"
    description = f"Description: {weather_data['weather'][0]['description']}"
    engine.say(weather)
    print(weather)
    engine.say(temp)
    print(temp)
    engine.say(feelslike)
    print(feelslike)
    engine.say(humidity)
    print(humidity)
    engine.say(description)
    print(description)
    engine.runAndWait()
else:
    engine.say("No such city of my knowledge.")
    engine.runAndWait()
    f"Error: {weather_data['message']}"
