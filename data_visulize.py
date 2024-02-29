
import matplotlib.pyplot as plt



def plot(avg_temp):
    y_axis = []
    x_axis = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec', 'Jan-2024', 'Feb-2024']
    for temp in avg_temp: 
        temp= float(temp.strip('°'))
        
        y_axis. append(temp)
    
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs[0].plot(x_axis,y_axis, marker='o', linestyle='-',color='blue')
    axs[0].set_title("Average Monthly Temperatures of The City Irvine from Mar 2023 to Feb 2024")
    axs[0].set_xlabel("Months")
    axs[0].set_ylabel("Temperature (°C)")
    axs[0].tick_params(axis = 'x',rotation=45)
   
    axs[1].bar(x_axis, y_axis, color='orange')
    axs[1].set_title("Average Monthly Temperatures of The City Irvine ';l,./,,./from Mar 2023 to Feb 2024")
    axs[1].set_xlabel("Months")
    axs[1].set_ylabel("Temperature (°C)")
    axs[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()



