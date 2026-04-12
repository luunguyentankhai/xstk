import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config

class Matrix_corr:
    def __init__(self, process_df):
        self.Data = process_df

    def plt_correlation_matrix(self):
        numberial_data = self.Data.select_dtypes(include=['int64', 'float64'])

        corr_matrix = numberial_data.corr()

        plt.figure(figsize=(10,8))

        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Heatmap ma tran tuong quan giua cac bien lien tuc")
        plt.savefig(config.Assets / "Matrix_corr.png", dpi=300, bbox_inches='tight')