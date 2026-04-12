import pandas as pd


class Statistic:
    def __init__(self, processed_df):
        self.Data = pd.read_csv(processed_df)

    def describe_numberical_data(self):
        Numberical_stat = self.Data[
            [
                "layer_height",
                "wall_thickness",
                "infill_density",
                "nozzle_temperature",
                "bed_temperature",
                "print_speed",
                "fan_speed",
                "tension_strenght",
            ]
        ]

        Describe_stat = Numberical_stat.describe()

        print(Describe_stat)

    def describe_categorical_data(self):
        print(self.Data["infill_pattern"].value_counts())
        print("-----------------------------------")
        print(self.Data["material"].value_counts())
