import os


def create_folders(base_dir):
    os.makedirs(base_dir, exist_ok=True)

    # Tạo các thư mục từ 60_30 đến 35_5
    for i in range(200, 9, -10):
        folder_name = f"{i}_{i}"
        os.makedirs(os.path.join(base_dir, folder_name), exist_ok=True)

    # # Tạo các thư mục từ 34_5 đến 10_5
    # for i in range(34, 9, -1):
    #     folder_name = f"{i}_5"
    #     os.makedirs(os.path.join(base_dir, folder_name), exist_ok=True)

    # print("Folders created successfully.")


base_dir = "D:\\SV\\HK6\\Algorithms and Analysis\\Maze\\SourceImg\\Maze\\SquareMatrix"
create_folders(base_dir)
