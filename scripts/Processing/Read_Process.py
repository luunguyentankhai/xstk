from pathlib import Path
import config
import pandas as pd
import main

'''
    file này chúng ta viết 3 hàm đó là :
        
        + Read_Data: hàm này để in ra dữ liệu được đọc từ file dữ liệu
        chúng ta sẽ đọc 10 dòng đầu của file dữ liệu
        
        + check_missing_data : hàm này dùng để kiểm thử rằng trong file dữ liệu
        có dòng nào bị NULL không chúng ta sẽ tính toán tỉ lệ và đếm xem có bao nhiêu dòng bị NULL
        
        + data_preprocessing: đây là một hàm rất quan trọng, vì chúng ta sẽ tiền xử lý
        dữ liệu trong hàm này để chuẩn bị tính toán
'''

class RP:
    def __init__(self):
        self.Data = config.Data_File
        self.Read = pd.read_csv(self.Data)
        self.df_eda = None
        self.df_of_model = None

    def Read_Data(self):
        self.Read.info()
        print(f"{self.Read.head(10)}")

    def check_missing_data(self):
        missing_counting = self.Read.isnull().sum()
        missing_percent = (missing_counting / len(self.Read))

        missing_sumary = pd.DataFrame(
            {
                'NULL Counting': missing_counting,
                'NULL %' : missing_percent
            }
        )
        return missing_sumary

    def data_preprocessing(self):

        # chuyển đổi 2 cột "infill_pattern", "material" thành dạng "category"
        self.Read['infill_pattern'] = self.Read['infill_pattern'].astype('category')
        self.Read['material'] = self.Read['material'].astype('category')

        self.df_eda = self.Read.copy()
        '''
            Chuyển đổi 2 cột trên từ "category" thành "dummy variable" để tính toán
            cho hồi quy tuyến tính
        '''
        
        self.df_of_model = pd.get_dummies(
            self.Read,
            columns=['infill_pattern', 'material'],
            dtype=int,
            drop_first=True
        )

        return self.df_eda,self.df_of_model

        
