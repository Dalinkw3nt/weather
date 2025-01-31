import requests

api_key = '9a1f76da1f91fefabb6a98c6fe51f217'

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metris&&APPID={api_key}")
if weather_data.json()['cod'] == '404':
    print ("No city found")
else: 
    print(weather_data.json())