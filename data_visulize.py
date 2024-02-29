
import matplotlib.pyplot as plt
import numpy as np
import json

# x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928,
#      67317, 68748, 73752]

# plt.plot(x, y)
# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")
# plt.title('Median Salary (USD) by Age')
# plt.show()


def visulize():
    data_temps = []
    with open('/Users/liyuanyuan/Desktop/GitHub/wp_4/chino.txt', 'r') as file:
        print("open file")
        data = json.load(file) 

    for tp in data["data"]:
        data_temps.append([tp["datetime"], tp["max_temp"]])

    with open('temp.txt', 'w') as f:
            

        json.dump(data_temps, f, indent= 4)



def main():
    
    visulize()

if __name__ == '__main__':
    main()

