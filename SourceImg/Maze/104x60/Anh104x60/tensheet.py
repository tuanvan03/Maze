import pandas as pd

# Đường dẫn đến file Excel
file_path = 'D:\DaiHoc\HK6\TKDGTT\Project\Maze\SourceImg\Maze\\104x60\Type (1)\\file_hop_nhat.xlsx'

# Sử dụng pandas để đọc file Excel và lấy tên các sheet
excel_file = pd.ExcelFile(file_path)

# Lấy tên các sheet
sheet_names = excel_file.sheet_names

# In tên các sheet
print("Tên các sheet trong file Excel là:")
for sheet in sheet_names:
    print(sheet)
