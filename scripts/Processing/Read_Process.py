from pathlib import Path
import config
import pandas as pd
import main

class RP:
    def __init__(self):
        self.Data = config.Data_File
        self.Read = pd.read_csv(self.Data)
        self.preprocessing = None

    def Read_Data(self):
        self.Read.info()
        print(f"{self.Read.head(5)}")
        print(f"{self.Read.tail(5)}")

    def check_missing_data(self):
        missing_counting = self.Read.isnull().sum()
        missing_percent = (missing_counting / len(self.Read))

        missing_sumary = pd.DataFrame(
            {
                'So luong Null': missing_counting,
                'Ti le Null' : missing_percent
            }
        )
        return missing_sumary

    def data_preprocessing(self):

        # chuyển đổi 2 cột "infill_pattern", "material" thành dạng "category"
        self.Read['infill_pattern'] = self.Read['infill_pattern'].astype('category')
        self.Read['material'] = self.Read['material'].astype('category')

        '''
            Chuyển đổi 2 cột trên từ "category" thành "dummy variable" để tính toán
            cho hồi quy tuyến tính
        '''
        
        self.preprocessing = pd.get_dummies(
            self.Read,
            columns=['infill_pattern', 'material'],
            dtype=int,
            drop_first=True
        )

        return self.preprocessing

        
