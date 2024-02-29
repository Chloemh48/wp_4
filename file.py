from rereive_data import get_daily_weather_data
import json
import datetime

def deal_file():

    USER_API_KEY = "9c605351de014c7aab50b15eeaef6e14"
    city = input("Enter City           : ")
    state = input("Enter State          : ")
    country = input("Enter Country        : ")
    filename_out = input("Enter filename to save data: ")
    dateend = datetime.date.today()
    datestart = dateend - datetime.timedelta(days=365)
    weather_data = get_daily_weather_data(city, state, country,
                                          str(datestart), str(dateend),
                                          USER_API_KEY)
    file_out = open(filename_out, "w")
    json.dump(weather_data, file_out)
    file_out.close()
