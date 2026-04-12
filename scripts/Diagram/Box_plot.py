import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config

class Box:
    def __init__(self, process_df):
        self.Data = process_df


    def plt_Box_plot(self):
        for var in config.dependent_vars:
            plt.figure(figsize=(8,5))
            sns.boxplot(x='material', y=var, data=self.Data)
            plt.title(f"BoxPlot {var} theo Material")
            file_name = config.Assets / f"BoxPlot_{var}_theo_Material.png"
            plt.savefig(file_name,dpi=300,bbox_inches='tight')
        
        for var in config.dependent_vars:
            plt.figure(figsize=(8,5))
            sns.boxplot(x='infill_pattern', y=var, data=self.Data)
            plt.title(f"BoxPlot {var} theo Infill_Pattern")
            file_name = config.Assets / f"BoxPlot_{var}_theo_Infill_Pattern.png"
            plt.savefig(file_name,dpi=300,bbox_inches='tight')
        