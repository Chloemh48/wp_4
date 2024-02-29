import urllib.request
from urllib.parse import quote
import json
import datetime

# import datetime
import ssl


def get_daily_weather_data(City: str, State: str, Country: str,
                           Datestart: str, Dateend: str, Api_key) -> dict:
    
    context = ssl._create_unverified_context()
    url = "https://api.weatherbit.io/v2.0/history/daily?city=" + City + \
               "," + State + "&country=" + Country + "&start_date=" + \
               Datestart + "&end_date=" + Dateend + "&key=" + Api_key
    

    with urllib.request.urlopen(url, context=context) as response:
        source = response.read()
        response.close()
        api_data_obj = json.loads(source)
        return api_data_obj
    

def deal_file():

    USER_API_KEY = "9c605351de014c7aab50b15eeaef6e14"
    city = input("Enter The City           : ")
    state = input("Enter State          : ")
    country = input("Enter Country        : ")
    filename_out = input("Enter filename to save data: ")
    dateend = datetime.date.today()
    datestart = dateend - datetime.timedelta(days=365)

    city_encoded = quote(city)
    state_encoded = quote(state)
    country_encoded = quote(country)
   
    weather_data = get_daily_weather_data(city_encoded, state_encoded, country_encoded,
                                          str(datestart), str(dateend),
                                          USER_API_KEY)
    file_out = open(filename_out, "w")
    with open(file_out, 'w') as f:

        json.dump(weather_data, file_out)

