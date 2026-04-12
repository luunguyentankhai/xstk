from pathlib import Path

Base_Path = Path(__file__).resolve().parent
Raw_Data_Path = Base_Path / "data" / "raw"
Processed_Data_Path = Base_Path / "data" / "processed"
Data_File = Raw_Data_Path / "data.csv"

DEBUG = True
VERSION = "1.0.0"