import urllib.request
import json
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
    
