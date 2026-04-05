from pathlib import Path
from scripts.pulldata import Pulldata
import pandas as pd
import os

#get data
if Pulldata():
    Pulldata()

Curr_dir = Path(__file__).resolve().parent

Data_dir = Curr_dir / "data" / "raw"

df = pd.read_csv(os.path.join(Data_dir, "data.csv"))

print(df.head(25))