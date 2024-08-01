import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "" #I removed my API key for privacy purposes
CITY = input("Please enter a city to view the weather: ").upper()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()

    if "main" in data and "weather" in data and "wind" in data and "sys" in data:
        temp_kelvin = data["main"]["temp"]
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = data["main"]["feels_like"]
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        sunrise_time = dt.datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"])
        sunset_time = dt.datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"])

        print(f"Temperature in {CITY}: {temp_celsius:.2f}° C or {temp_fahrenheit:.2f}°F")
        print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}° C or {feels_like_fahrenheit:.2f}°F")
        print(f"Humidity in {CITY}: {humidity}%")
        print(f"Wind speed in {CITY}: {wind_speed}km/h")
        print(f"General Weather in {CITY}: {description}")
        print(f"Sun rises in {CITY} at {sunrise_time} local time.")
        print(f"Sun sets in {CITY} at {sunset_time} local time.")
    else:
        print("Error: Some expected keys are missing in the response.")
        print("Response Data:", data)

except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")
except KeyError as e:
    print(f"KeyError: {e} - Check the response structure.")
except Exception as e:
    print(f"An error occurred: {e}")


#Asking user if they want to print the full data report
print("----------------------------------")
answer = input("Do you want the full data report? ").upper()
if(answer == "YES"):
    # Print the full response for debugging
    print("Full Response:", data)

else:
    print("Thank you for using our services.")