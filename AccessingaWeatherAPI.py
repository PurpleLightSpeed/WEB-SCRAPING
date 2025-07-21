import requests, os, json
from dotenv import load_dotenv

load_dotenv()

city_name = "San Francisco"
state_code = "CA"
country_code = "US"
API_key = os.getenv("open_weather_map_api_key")
response = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}")
# print(response.text) # This is a python string
response_data = json.loads(response.text)
# print(response_data) # This is a python data structure

print(response_data[0]["lat"])
print(response_data[0]["lon"])

lat = json.loads(response.text)[0]["lat"]
lon = json.loads(response.text)[0]["lon"]
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}")
response_data = json.loads(response.text)
# print(response_data)
main_temp = response_data["main"]["temp"]
print(round(main_temp - 273.15, 1)) # Convert Kelvin to Celsius.
print(round(main_temp * (9 / 5) - 459.67, 1)) # Convert Kelvin to Fahrenheit.

print(response_data['weather'][0]['main']) # Holds a string description, such as 'Clear', 'Rain', or 'Snow'
print(response_data['weather'][0]['description']) # Holds a more descriptive string, such as 'light rain', 'moderate rain', or 'extreme rain'
print(response_data['main']['temp']) # Holds the current temperature in Kelvin
print(response_data['main']['feels_like']) # Holds the human perception of the temperature in Kelvin
print(response_data['main']['humidity']) # Holds the humidity as a percentage

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}")
response_data = json.loads(response.text)
# Now you can safely access response_data['list']

response_data['list'] # Holds a list of dictionaries containing the weather predictions for a given time.
response_data['list'][0]['dt'] # Holds a timestamp in the form of a Unix epoch float. Pass this value as an argument to datetime.datetime.fromtimestamp() to obtain the timestamp as a datetime object. Chapter 19 discusses Python’s datetime module in more detail.
response_data['list'][0]['main'] # Holds a dictionary with keys like 'temp', 'feels_like', 'humidity', and others.
response_data['list'][0]['weather'][0] # Holds a dictionary of descriptions with keys like 'main', 'description', and others.



