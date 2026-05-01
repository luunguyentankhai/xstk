from pathlib import Path


'''
    File config.py chứa các địa chỉ của dữ liệu truyền về 2 thư mục là raw chứa
    dữ liệu thô chưa xử lý, processed để chứa các dữ liệu đã xử lý và Assets để chứa
    các bảng mô hình.
'''
Base_Path = Path(__file__).resolve().parent
Raw_Data_Path = Base_Path / "data" / "raw"
Processed_Data_Path = Base_Path / "data" / "processed"
Data_File = Raw_Data_Path / "data.csv"

#Diagram
Assets = Base_Path / "data" / "Assets"


# dependent_vars là biến để xác định các biến phụ thuộc
dependent_vars =  ["roughness", "tension_strenght", "elongation"]

# independent_vars là biến để xác định các biến độc lập
independent_vars = ["layer_height","wall_thickness","infill_density","nozzle_temperature","bed_temperature","print_speed","fan_speed"]


DEBUG = True
VERSION = "1.0.0"
