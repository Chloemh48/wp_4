
import matplotlib.pyplot as plt


def plot(avg_aqi):
    """
    The plot() function will create two diagrams: a bar chart and
    a plot chart, each displaying the daily average air quality index
    values from February 1, 2024, to February 29, 2024. The parameter is ave_aqi,
    which represents the daily average AQI, and its type is 'list'.
    """
    y_axis = []
    x_axis = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              '11', '12', '13', '14', '15', '16', '17', '18', '19',
              '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
    for i in avg_aqi:
        i = float(i.strip('°'))

        y_axis. append(i)

    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    # Plot chart
    axs[0].plot(x_axis, y_axis, marker='o', linestyle='-', color='blue')
    axs[0].set_title("Average Daily Air Quality of Chino in Feburay 2024")
    axs[0].set_xlabel("Daily")
    axs[0].set_ylabel("Air Quality Index Value")
    axs[0].tick_params(axis='x', rotation=45)

    # Bar chart
    axs[1].bar(x_axis, y_axis, color='orange')
    axs[1].set_title("Average Daily Air Quality of Chino in Feburay 2024")
    axs[1].set_xlabel("Daily")
    axs[1].set_ylabel("Air Quality Index Value")
    axs[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()
