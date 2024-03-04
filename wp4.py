import data_visulize as dv
from data_into_file import cal_mean_temp


def main():
    
    avg_temp = cal_mean_temp()
    print(avg_temp)
    
    dv.plot(avg_temp)

   
    
if __name__ == "__main__":
    print("test")
    main()
