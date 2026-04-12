from scripts.pulldata import Pulldata
from scripts.Processing import Read_Process
import pandas as pd

class Main:
    def __init__(self):
        self.RP = Read_Process.RP()

def main():
    Pulldata()
    xstk = Main()
    #xstk.RP.Read_Data()
    #print("---------------------------------")
    #xstk.RP.check_missing_data()
    # print("---------------------------------")
    print(xstk.RP.data_preprocessing())
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error : {e}")
    finally:
        pass
