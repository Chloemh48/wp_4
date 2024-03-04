
import urllib.request
import json
import ssl
from datetime import datetime
from collections import defaultdict

def get_air_quality():
    
    context = ssl._create_unverified_context()
    API_KEY = 'eacd6c69cbec4827a22c2f8c0b5daab8'  # Replace with your actual API key

    # Constructing the URL with the postal code and country code
    url = f"https://api.weatherbit.io/v2.0/history/airquality?postal_code=91710&country=US&start_date=2024-02-01&end_date=2024-02-29&tz=local&key={API_KEY}"
    
    print("Requesting URL:", url)  # Print the URL to verify its correctness

    try:
        with urllib.request.urlopen(url, context=context) as response:
            source = response.read()
            api_data_obj = json.loads(source)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error encountered: {e.code} - {e.reason}")
        return

    filename_out = input("Enter the file name you wish to save:")

    with open(filename_out, 'w') as file_out:
        json.dump(api_data_obj, file_out)
    return filename_out


def cal_mean_aqi(filename_out):
    print('Data is loading...')
    try:
        with open(filename_out,'r') as file:

            print("File is openning...")
            data = json.load(file)  
    except Exception as e:
        print(f'Error: {e}')
        return

    # aqi stands for air quality index value
    data_aqi = []
    for aqi in data["data"]:
        
        data_aqi.append([aqi["aqi"],aqi['datetime']])

    with open('aqi.txt', 'w') as f:
        json.dump(data_aqi, f, indent=4)

    daily_aqi = defaultdict(lambda: {'sum': 0, 'count': 0})


    for item in data_aqi:
        value, date_str = item[0], item[1] 
        date_obj = datetime.strptime(date_str.split(':')[0], "%Y-%m-%d")
        daily = date_obj.strftime('%Y-%m-%d')  
        
        # Process dates from 2023-01-01 to  2023-01-08
        if datetime(2024, 2, 1) <= date_obj <= datetime(2024, 2, 29):
            daily_aqi[daily]['sum'] += value
            daily_aqi[daily]['count'] += 1

    # Calculate average aqi per day
    avg_aqi = []
    for daily, value in sorted(daily_aqi.items()):
        average_aqi = value['sum'] / value['count']
        print(f"Mean aqi for {daily}: {average_aqi:.2f}°")
        avg_aqi.append(f'{average_aqi:.2f}°')
  
    return avg_aqi


