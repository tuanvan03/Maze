import os
import cv2
import time
import psutil
import pandas as pd
from PIL import Image
import numpy as np
from bfs_class import BreadthFirst
from settings import wall_nodes_coords_list

from bfs_class import *
from dfs_class import *
from astar_class import *
from dijkstra_class import *
from bidirectional_class import *


# from insert_maze import *
# from settings import *
# Đọc ảnh
def read_image(image_path):
    file_list = os.listdir(image_path)

    # Chỉ lấy các tệp có định dạng ảnh (vd: .jpg, .png)
    image_files = [
        os.path.join(image_path, file)
        for file in file_list
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))
    ]
    result = []
    image_names = []  # Tạo một list để lưu tên của các ảnh
    for file_path in image_files:
        img = Image.open(file_path)
        target_size = (104, 60)
        img_resized = img.resize(target_size, resample=Image.BILINEAR)

        # Convert the resized image to a NumPy array
        matrix = np.array(img_resized)

        # Convert to binary matrix (0 for white, 1 for black)
        binary_matrix = (matrix[:, :, 0] > 128).astype(int)
        # print(len(binary_matrix), len(binary_matrix[0]))
        result.append(binary_matrix)

        # Lưu tên của ảnh vào list
        image_names.append(
            os.path.splitext(os.path.basename(file_path))[0]
        )  # Lấy tên của ảnh mà không có phần mở rộng

    return result, image_names  # Trả về kết quả và tên của các ảnh


def main():
    image_path = "D:\\SV\\HK6\\Algorithms and Analysis\\Maze\\SourceImg\\Maze\\New\\day"
    binary_img, image_names = read_image(
        image_path
    )  # Lấy binary_img và image_names từ hàm read_image
    count = 0
    for matrix, image_name in zip(
        binary_img, image_names
    ):  # Sử dụng hàm zip để lặp qua binary_img và image_names cùng một lúc
        print("Dang doc anh thu: ", count)
        count += 1
        data = []
        # print(matrix)
        start = (2, 3)
        end = (105, 60)
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
                "Maze": image_name,  # Lưu tên của ảnh vào cột "Maze"
            }
        )

        dfs = DepthFirst(
            app=None,
            start_node_x=start[0],
            start_node_y=start[1],
            end_node_x=end[0],
            end_node_y=end[1],
            wall_pos=wall_pos,
        )

        start_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)
        start_time = time.time()
        dfs.dfs_execute()
        end_time = time.time()
        end_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)

        # Tính toán thời gian và bộ nhớ
        execution_time = end_time - start_time
        memory_usage = end_memory_usage - start_memory_usage
        data.append(
            {
                "Name algorithm": "DFS",
                "Runtime (s)": execution_time,
                "Memory Usage (MB)": memory_usage,
                "Movement": len(dfs.route),
                "Maze": image_name,  # Lưu tên của ảnh vào cột "Maze"
            }
        )

        a_star = AStar(
            app=None,
            start_node_x=start[0],
            start_node_y=start[1],
            end_node_x=end[0],
            end_node_y=end[1],
            wall_pos=wall_pos,
        )

        start_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)
        start_time = time.time()
        a_star.astar_execute()
        end_time = time.time()
        end_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)

        # Tính toán thời gian và bộ nhớ
        execution_time = end_time - start_time
        memory_usage = end_memory_usage - start_memory_usage
        data.append(
            {
                "Name algorithm": "A star",
                "Runtime (s)": execution_time,
                "Memory Usage (MB)": memory_usage,
                "Movement": len(a_star.route),
                "Maze": image_name,  # Lưu tên của ảnh vào cột "Maze"
            }
        )

        dj = Dijkstra(
            app=None,
            start_node_x=start[0],
            start_node_y=start[1],
            end_node_x=end[0],
            end_node_y=end[1],
            wall_pos=wall_pos,
        )

        start_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)
        start_time = time.time()
        dj.dijkstra_execute()
        end_time = time.time()
        end_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)

        # Tính toán thời gian và bộ nhớ
        execution_time = end_time - start_time
        memory_usage = end_memory_usage - start_memory_usage
        data.append(
            {
                "Name algorithm": "Dijkstra",
                "Runtime (s)": execution_time,
                "Memory Usage (MB)": memory_usage,
                "Movement": len(dj.route),
                "Maze": image_name,  # Lưu tên của ảnh vào cột "Maze"
            }
        )

        bdi = Bidirectional(
            app=None,
            start_node_x=start[0],
            start_node_y=start[1],
            end_node_x=end[0],
            end_node_y=end[1],
            wall_pos=wall_pos,
        )

        start_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)
        start_time = time.time()
        bdi.bidirectional_execute()
        end_time = time.time()
        end_memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024**2)

        # Tính toán thời gian và bộ nhớ
        execution_time = end_time - start_time
        memory_usage = end_memory_usage - start_memory_usage
        data.append(
            {
                "Name algorithm": "Bidirectional",
                "Runtime (s)": execution_time,
                "Memory Usage (MB)": memory_usage,
                "Movement": len(bdi.route_f) + len(bdi.route_r),
                "Maze": image_name,  # Lưu tên của ảnh vào cột "Maze"
            }
        )
        try:
            existing_df = pd.read_excel("big_maze.xlsx")
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Nối dữ liệu mới vào DataFrame hiện có
        df = pd.concat([existing_df, pd.DataFrame(data)], ignore_index=True)
        # Ghi lại DataFrame vào file Excel
        df.to_excel("big_maze.xlsx", index=False)


if __name__ == "__main__":
    main()
