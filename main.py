from scripts.pulldata import Pulldata
from scripts.Processing import Read_Process,Statistics_Table
from scripts.Diagram import Matrix_corr,Scatter_plot,Box_plot,Histogram,Models_Diagnostics
from scripts.Models import OLS,Statistical_Diagnostics,VIF_check
import config
import pandas as pd
import warnings



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
        self.MD = Models_Diagnostics

        #Models
        self.OLS = OLS
        self.SD = Statistical_Diagnostics
        self.VIF = VIF_check

def main():
    Pulldata()
    xstk = Main()
    # xstk.RP.Read_Data()
    # print("\n---------------------------------\n")
    # xstk.RP.check_missing_data()
    # print("\n---------------------------------\n")
    eda, preprocessing = xstk.RP.data_preprocessing()
    # print(eda)
    # print("\n---------------------------------\n")
    # print(preprocessing)
    # print("\n---------------------------------\n")
    # xstk.MX.Matrix_corr(eda).plt_correlation_matrix()
    # xstk.SP.Scatter(eda).plt_Scatter_plot()
    # xstk.BX.Box(eda).plt_Box_plot()
    # xstk.HS.Histogram(eda).plt_Histogram()

    cols_to_remove = ['material_ABS', 'fan_speed']
    preprocessing = preprocessing.drop(columns=cols_to_remove, errors='ignore')

    fit_models, useless = xstk.OLS.MultipleRegression(preprocessing).fit_models()
    
    # diagnostics_plt = xstk.MD.ModelDiagnostic(fit_models)

    # diagnostics_plt.plt_scatter_residuals()
    # diagnostics_plt.plt_QQ_normality()
    for i in config.dependent_vars:
        xstk.SD.StatisticalDiagnostics(fit_models,i).Test_run()
        xstk.VIF.VIFChecker(preprocessing,useless,i).Check()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error : {e}")
    finally:
        pass
