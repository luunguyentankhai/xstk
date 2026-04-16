import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import config


class ModelDiagnostic:
    def __init__(self, finally_models):
        self.models = finally_models

    def plt_scatter_residuals(self):
        for target_var in self.models.keys():

            model = self.models[target_var]

            residuals = model.resid
            predicted = model.fittedvalues

            # residuals vs predicted
            plt.figure(figsize=(7, 5))
            sns.scatterplot(x=predicted, y=residuals, color="teal", alpha=0.7)
            plt.axhline(0, color="red", linestyle="--")
            plt.title("Residuals vs Predicted")

            plt.xlabel(f"Predicted {target_var}")
            plt.ylabel(f"Residuals")

            file_name = config.Assets / f"Residuals_vs_Predicted_{target_var}.png"
            plt.savefig(file_name,dpi=300,bbox_inches="tight")

    def plt_QQ_normality(self):
        for target_var in self.models.keys():

            model = self.models[target_var]

            residuals = model.resid

            fig, ax = plt.subplots(figsize=(7, 5))
            sm.qqplot(residuals, line="45", fit=True, ax=ax, color="teal", alpha=0.7)

            ax.set_title(f"Normal QQ_plt of residuals")
            ax.set_xlabel(f"Theoretical Quantiles")
            ax.set_ylabel(f"Ordered Values")

            file_name = config.Assets / f"Normal QQ_plt of residuals_of_{target_var}.png"
            plt.savefig(file_name,dpi=300,bbox_inches="tight")


