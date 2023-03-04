"""
overall task:
I would like a daily email
        hint: https://stackoverflow.com/questions/31011179/converting-json-to-html-table-in-python

The email should contain:
- the maximum 'Shortwave Solar Radiation' for the day in purfleet
- the maximum 'Shortwave Solar Radiation' for the day in forest hill
- a cat fact
- the current 'CPIUS - United States - Consumer price index'

please save the email to an HTML file (json is fine)
and save a copy of the filename to a database as a record that the email has been created for today

how to:

    to get 'Shortwave Solar Radiation':
    https://open-meteo.com/en/docs#api_form

    - purfleet
        lat: 52.52
        long: 13.41
    - forest hill
        lat: 51.4431
        long: -0.04178

    to get 'CPIUS - United States - Consumer price index':
    https://www.econdb.com/api/series/?page=1&search=inflation


    lots of free APIs: (will help with cat facts)
    https://github.com/public-apis/public-apis

    sqlite:
    https://www.tutorialspoint.com/sqlite/sqlite_python.htm
"""
import datetime

import requests as requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")

print(response.status_code)

class BaseApiInterface:
    url = None
    def get_data(self):
        pass
    def update_url(self, url:str):
        pass
    def update_datetime(self, date:datetime.datetime):
        pass

class Weather(BaseApiInterface):
    def __init__(self, url:str, lat:str, long:str):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.lat = ''
        self.long = ''
    def get_data(self):
        # 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m'
        # 'https://api.open-meteo.com/v1/forecast?longditude=52.52&longitude=13.41&hourly=temperature_2m'
        param_dict = {
            'latitude': self.lat,
            'longitude': self.long,
        }
        response = requests.get(self.url, params=param_dict)

class Catpics:
    def __init__(self):
        pass

class Cpius:
    api_token = "126867625166bb43a51bde9f0c0d50fc4d1d6bab"
    def __init__(self, url:str):
        self.url = f"https://www.econdb.com/api/series/CPIFR/?token={self.api_token}&format=json"
    def get_data(self):
        response = requests.get(self.url)
        if not response.ok:
            raise Exception(response)
        data = response.json()
        return data



purfleet_weather = Weather(52.52, 13.41)
forest_hill_weather = Weather(51.4431, -0.04178)

