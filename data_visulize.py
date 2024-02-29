
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime
from collections import defaultdict


def visualize():
    with open('/Users/liyuanyuan/Desktop/GitHub/wp_4/ir.txt', 'r') as file:
        print("Open file")
        data = json.load(file)  


    data_temps = []
    for tp in data["data"]:
        daily_mean_temp = (tp["max_temp"] + tp['min_temp']) / 2
        
        data_temps.append([tp["datetime"],daily_mean_temp])

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
    
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs[0].plot(x_axis,y_axis, marker='o', linestyle='-',color='blue')
    axs[0].set_title("Average Monthly Temperatures of City Irvine from Mar 2023 to Feb 2024")
    axs[0].set_xlabel("Months")
    axs[0].set_ylabel("Temperature (°C)")
    axs[0].tick_params(axis = 'x',rotation=45)
   
    axs[1].bar(x_axis, y_axis, color='orange')
    axs[1].set_title("Average Monthly Temperatures of City Irvine ';l,./,,./from Mar 2023 to Feb 2024")
    axs[1].set_xlabel("Months")
    axs[1].set_ylabel("Temperature (°C)")
    axs[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()


def main():
    avg_temp = visualize()
    print(avg_temp)
    
    plot(avg_temp)

   

if __name__ == '__main__':
    main()

