import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config

class Histogram:
    def __init__(self, process_df):
        self.Data = process_df

    def plt_Histogram(self):
        for var in config.dependent_vars:
            plt.figure(figsize=(6,4))
            sns.histplot(self.Data[var], bins=10, kde=True, color='skyblue')
            plt.title(f"Histogram of {var}")
            plt.xlabel(var)
            plt.ylabel('Tan so')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            file_name = config.Assets / f"Histogram of {var}"
            plt.savefig(file_name, dpi=300, bbox_inches='tight')