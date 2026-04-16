import pandas as pd
import statsmodels.api as sm
from scripts.Models import VIF_check
import config 

class MultipleRegression:
    def __init__(self, process_df):
        self.Data = process_df

        self.X_full = self.Data.drop(columns=config.dependent_vars)

        self.X_full = sm.add_constant(self.X_full)

        self.finally_models = {}

        self.useless = {}

    def fit_models(self):
        for target in config.dependent_vars:

            y = self.Data[target]

            model_full = sm.OLS(y,self.X_full).fit()
            print("ALL VARIABLE")
            print(model_full.summary())

            p_value = model_full.pvalues

            p_value = p_value.drop('const', errors='ignore')

            useless_values = p_value[p_value>0.05].index.tolist()

            self.useless[target] = useless_values.copy()

            if useless_values:
                print(useless_values)

                X_refined= self.X_full.drop(columns=useless_values)

                model_refined=sm.OLS(y,X_refined).fit()

                print(model_refined.summary())

                self.finally_models[target] = model_refined
            else:
                self.finally_models[target] = model_full
        
        return self.finally_models,self.useless