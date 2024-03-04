import json
from datetime import datetime
from collections import defaultdict


def cal_mean_aqi(filename_out):
    """
    The cal_mean_aqi function pulls air quality values at different
    times of the day from the saved JSON file and calculates the
    average daily air quality value. The parameter is filename_out,
    which refers to the saved JSON file, and its type is 'file'.

    """
    print('Data is loading...')
    try:
        with open(filename_out, 'r') as file:

            print("File is openning...")
            data = json.load(file)
    except Exception as e:
        print(f'Error: {e}')
        return

    # aqi stands for air quality index value
    data_aqi = []
    for aqi in data["data"]:
        data_aqi.append([aqi["aqi"], aqi['datetime']])

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
