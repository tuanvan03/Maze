import pandas as pd
import os

# Đường dẫn đến thư mục chứa các file Excel
folder_path = 'D:\DaiHoc\HK6\TKDGTT\Project\Maze\SourceImg\Maze\Type (1)\Type (1)'

# Tạo một danh sách chứa tên các file Excel
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Tạo một writer để ghi dữ liệu vào file Excel mới
with pd.ExcelWriter('file_hop_nhat.xlsx', engine='openpyxl') as writer:
    for file in excel_files:
        # Đọc từng file Excel
        df = pd.read_excel(os.path.join(folder_path, file))
        # Lưu sheet vào file hợp nhất với tên sheet là tên file (không có phần mở rộng)
        sheet_name = os.path.splitext(file)[0]
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Hoàn thành hợp nhất các file Excel!")
