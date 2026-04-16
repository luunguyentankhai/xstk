import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np
import warnings
import config

class VIFChecker:
    def __init__(self, process_df,values,Target_var):
        self.Data = process_df
        self.Select_values = values
        self.Target = Target_var

    def Check(self):
        X = self.Data.drop(columns=config.dependent_vars)
        X = X.drop(columns=self.Select_values[self.Target])        

        vif_data = pd.DataFrame()
        vif_data["Variable"]= X.columns
        vif_data["VIF"]= [variance_inflation_factor(X.values,i) for i in range(X.shape[1])]
            
        print(vif_data)
        print(f"{'='*50}")