from scripts.pulldata import Pulldata
from scripts.Processing import Read_Process,Statistics_Table
from scripts.Diagram import Matrix_corr,Scatter_plot,Box_plot,Histogram
import config
import pandas as pd

class Main:
    def __init__(self):
        #Read and Process
        self.RP = Read_Process.RP()
        
        #Statistics
        self.ST = Statistics_Table.Statistic(config.Data_File)
        
        #Diagram 
        self.MX = Matrix_corr
        self.SP = Scatter_plot
        self.BX = Box_plot
        self.HS = Histogram


def main():
    Pulldata()
    xstk = Main()
    xstk.RP.Read_Data()
    print("\n---------------------------------\n")
    xstk.RP.check_missing_data()
    print("\n---------------------------------\n")
    eda, preprocessing = xstk.RP.data_preprocessing()
    print(eda)
    print("\n---------------------------------\n")
    print(preprocessing)
    print("\n---------------------------------\n")
    xstk.MX.Matrix_corr(eda).plt_correlation_matrix()
    xstk.SP.Scatter(eda).plt_Scatter_plot()
    xstk.BX.Box(eda).plt_Box_plot()
    xstk.HS.Histogram(eda).plt_Histogram()


    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error : {e}")
    finally:
        pass
