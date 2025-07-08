import requests
from dotenv import load_dotenv # to get the api key from .env
import os
from pprint import pprint

load_dotenv() # loads the environment file to the program so we can access them

def weatherApp():
    print("Welcome to my weather app0\n")
    CITY = input("Enter your city name: \n")

    request_url=f"https://api.openweathermap.org/data/3.0/weather?appid={os.getenv("API_KEY")}&q={CITY}&units='imperial'"

    weather_data = requests.get(request_url).json()
    pprint(weather_data)
weatherApp()