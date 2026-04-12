import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config

class Scatter:
    def __init__(self, process_df):
        self.Data = process_df

    def plt_Scatter_plot(self):
        for dep in config.dependent_vars:
            for indep in config.independent_vars:
                plt.figure(figsize=(6,4))
                sns.scatterplot(x=indep, y=dep, data=self.Data)
                plt.title(f"Scatter_plot: {dep} vs {indep}")
                plt.xlabel(indep)
                plt.ylabel(dep)

                #plt.show()

                file_name = config.Assets / f"Scatter_plot_{dep}_vs_{indep}.png"

                plt.savefig(file_name,dpi=300,bbox_inches='tight')

                plt.close()