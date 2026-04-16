import numpy as np
import pandas as pd
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.outliers_influence import variance_inflation_factor


class StatisticalDiagnostics:
    def __init__(self, finally_model, Target_var):
        self.models = finally_model
        self.target = Target_var

    def Test_run(self):
        model = self.models[self.target]

        X_data = model.model.exog
        print(f"{'='*50}")
        mean_resid = np.mean(model.resid)
        print(mean_resid)
        print(f"{'='*50}")
        dw_stat = durbin_watson(model.resid)
        print(dw_stat)
        print(f"{'='*50}")
        sta, pval_bp, T_sta, F_sta = het_breuschpagan(model.resid, X_data)
        labels = {
            "LM Statistic": [sta],
            "LM-Test p-value": [pval_bp],
            "F-Statistic": [T_sta],
            "FTest p-value": [F_sta],
        }
        df_result = pd.DataFrame(labels)
        print(df_result)
        print(f"{'='*50}")
