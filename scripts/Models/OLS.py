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

        #config.dependent_vars = "roughness, tension, elegation"
        for target in config.dependent_vars:

            y = self.Data[target]

            model_full = sm.OLS(y,self.X_full).fit()
            print("ALL VARIABLE")
            self.Resid(model_full)
            print(model_full.summary())
                       
            #lay gia tri p_value 
            p_value = model_full.pvalues
            
            #loai bo p_value cua const ra truoc
            p_value = p_value.drop('const', errors='ignore')
            
            #xac dinh cac p_value co gia tri lon hon 0.05
            useless_values = p_value[p_value>0.05].index.tolist()

            self.useless[target] = useless_values.copy()

            if useless_values:
                
                #xoa cai bien duoc chua trong useless_values
                X_refined= self.X_full.drop(columns=useless_values)
                
                #tinh toan lai hoi quy sau loai bo
                model_refined=sm.OLS(y,X_refined).fit()
                self.Resid(model_refined)
                print(model_refined.summary())
                

                self.finally_models[target] = model_refined
            else:
                self.finally_models[target] = model_full
        
        return self.finally_models,self.useless

    def Resid(self, model):
        residuals = model.resid
        res_summary = pd.DataFrame({
            "Min" : [residuals.min()],
            "1Q" : [residuals.quantile(0.25)],
            "Median" : [residuals.median()],
            "3Q" : [residuals.quantile(0.75)],
            "Max" : [residuals.max()]
            }) 

        print(f"{'='*50}")
        print("Residuals")
        print(res_summary.round(5).to_string(index=False))
        print(f"{'='*50}")
