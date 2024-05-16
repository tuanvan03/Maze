from bfs_class import *
from dfs_class import *
from astar_class import *
from dijkstra_class import *
from bidirectional_class import *
import cv2
import time
from insert_maze import *
import os
import psutil
import pandas as pd
from settings import *


# Doc anh
def read_image(image_path):
    file_list = os.listdir(image_path)

    # Chỉ lấy các tệp có định dạng ảnh (vd: .jpg, .png)
    image_files = [
        os.path.join(image_path, file)
        for file in file_list
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))
    ]
    result = []
    for file_path in image_files:
        img = Image.open(file_path)
        target_size = (104, 60)
        img_resized = img.resize(target_size, resample=Image.BILINEAR)

        # Convert the resized image to a NumPy array
        matrix = np.array(img_resized)

        # Convert to binary matrix (0 for white, 1 for black)
        binary_matrix = (matrix[:, :, 0] > 128).astype(int)
        print(len(binary_matrix), len(binary_matrix[0]))
        result.append(binary_matrix)

    return result


def main():
    image_path = "D:\\SV\\HK6\\Algorithms and Analysis\\Maze\\SourceImg\\Maze\\New"
    binary_img = read_image(image_path)
    count = 0
    for matrix in binary_img:
        # print(len(matrix))
        count += 1
        data = []
        print(matrix)
        start = (2, 4)
        end = (105, 59)
        wall_pos = wall_nodes_coords_list.copy()
        for j in range(104):
            for i in range(60):
                if matrix[i][j] == 0:
                    wall_pos.append((j + 2, i + 2))

        bfs = BreadthFirst(
            app=None,
            start_node_x=start[0],
            start_node_y=start[1],
            end_node_x=end[0],
            end_node_y=end[1],
            wall_pos=wall_pos,
        )
        print("Route_found : ", bfs.route_found)

        start_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)
        start_time = time.time()

        bfs.bfs_execute()

        end_time = time.time()
        end_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)

        # Tính toán thời gian và bộ nhớ
        execution_time = end_time - start_time
        memory_usage = end_memory_usage - start_memory_usage
        data.append(
            {
                "Name algorithm": "BFS",
                "Runtime (s)": execution_time,
                "Memory Usage (MB)": memory_usage,
                "Movement": len(bfs.route),
                "Maze": "maze" + str(count),
            }
        )
        try:
            existing_df = pd.read_excel("performance_data.xlsx")
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Nối dữ liệu mới vào DataFrame hiện có
        df = pd.concat([existing_df, pd.DataFrame(data)], ignore_index=True)
        # Ghi lại DataFrame vào file Excel
        df.to_excel("performance_data.xlsx", index=False)

        print("Route_found : ", bfs.route_found)
        print("Thời gian thực thi:", execution_time)
        print("Bộ nhớ cần dùng:", memory_usage)
        print("Bộ nhớ cần dùng:", len(bfs.route))


if __name__ == "__main__":
    main()
