
import retrieve_data as rd
import data_visulize as dv


def main():
    filename_out = rd.get_air_quality()

    if filename_out:
        avg_aqi = rd.cal_mean_aqi(filename_out)
        print(avg_aqi)
        
        dv.plot(avg_aqi)


if __name__ == "__main__":
    main()