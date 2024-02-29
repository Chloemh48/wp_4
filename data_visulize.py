
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime
from collections import defaultdict

# x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928,
#      67317, 68748, 73752]

# plt.plot(x, y)
# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")
# plt.title('Median Salary (USD) by Age')
# plt.show()


def visualize():
    with open('/Users/liyuanyuan/Desktop/GitHub/wp_4/chino.txt', 'r') as file:
        print("Open file")
        data = json.load(file)  


    data_temps = []
    for tp in data["data"]:
        
        data_temps.append([tp["datetime"], tp["max_temp"]])

    with open('temp.txt', 'w') as f:
        json.dump(data_temps, f, indent=4)

    monthly_temps = defaultdict(lambda: {'sum': 0, 'count': 0})


    for date_str, temp in data_temps:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        month_year = date_obj.strftime('%Y-%m')  # Format as 'YYYY-MM'
        
        # Process dates from March 2023 to February 2024
        if datetime(2023, 3, 1) <= date_obj <= datetime(2024, 2, 29):
            monthly_temps[month_year]['sum'] += temp
            monthly_temps[month_year]['count'] += 1

    # Calculate average temperatures per month
    avg_temp = []
    for month_year, temps in sorted(monthly_temps.items()):
        average_temp = temps['sum'] / temps['count']
        print(f"Average temperature for {month_year}: {average_temp:.2f}°")
        avg_temp.append(f'{average_temp:.2f}°')
    return avg_temp

def plot(avg_temp):
    y_axis = []
    x_axis = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec', 'Jan-2024', 'Feb-2024']
    for temp in avg_temp: 
        temp= float(temp.strip('°'))
        y_axis. append(temp)
    
    
    plt.plot(x_axis,y_axis)
    plt.title("Average Monthly Temperatures from Mar 2023 to Feb 2024")
    plt.xlabel("Months")
    plt.ylabel("plt.ylabel('Temperature (°C)')")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(x_axis, y_axis, color='orange')

    plt.title('Average Monthly Temperatures from Mar 2023 to Feb 2024')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.show()


def main():
    avg_temp = visualize()
    print(avg_temp)
    
    plot(avg_temp)

if __name__ == '__main__':
    main()

