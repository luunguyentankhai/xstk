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
        model = self.Data[self.Target]
        X = model.model.exog
        feature_names = model.model.exog_names

        vif_data = pd.DataFrame()
        vif_data["Variable"]= feature_names
        vif_data["VIF"]= [variance_inflation_factor(X,i) for i in range(X.shape[1])]
        
        vif_data = vif_data[vif_data["Variable"] != "const"]

        print(vif_data)
        print(f"{'='*50}")
