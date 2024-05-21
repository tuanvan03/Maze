import os
import time
import tracemalloc
import pandas as pd
from PIL import Image
import numpy as np
from settings import wall_nodes_coords_list
from bfs_class import BreadthFirst
from dfs_class import DepthFirst
from astar_class import AStar
from dijkstra_class import Dijkstra
from bidirectional_class import Bidirectional
import gc


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
        w, h = img.size
        target_size = (w // 10, h // 10)
        img_resized = img.resize(target_size, resample=Image.BILINEAR)

        # Convert the resized image to a NumPy array
        matrix = np.array(img_resized)

        # Convert to binary matrix (0 for white, 1 for black)
        binary_matrix = (matrix[:, :, 0] > 128).astype(int)
        result.append(binary_matrix)

        # Lưu tên của ảnh vào list
        image_names.append(os.path.splitext(os.path.basename(file_path))[0])

    return result, image_names  # Trả về kết quả và tên của các ảnh


def measure_memory_and_time(execute_func):
    tracemalloc.start()
    start_time = time.time()
    execute_func()
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    gc.collect()

    execution_time = end_time - start_time
    memory_usage = peak / (1024**2)
    return execution_time, memory_usage


def process_images_in_folder(image_path, output_excel):
    binary_img, image_names = read_image(image_path)
    all_data = []
    count = 1
    print(f"Start with {output_excel}")
    for matrix, image_name in zip(binary_img, image_names):
        print("Processing image number:", count)
        count += 1
        data = []
        wall_pos = []

        start = (1, 1)
        end = (len(matrix[0] - 2), len(matrix) - 2)
        for j in range(len(matrix[0] - 1)):
            for i in range(len(matrix) - 1):
                if matrix[i][j] == 0:
                    wall_pos.append((j, i))

        algorithms = [
            ("BFS", BreadthFirst, "bfs_execute"),
            ("DFS", DepthFirst, "dfs_execute"),
            ("AStar", AStar, "astar_execute"),
            ("Dijkstra", Dijkstra, "dijkstra_execute"),
            ("Bidirectional", Bidirectional, "bidirectional_execute"),
        ]

        for name, AlgoClass, method_name in algorithms:
            algo = AlgoClass(
                app=None,
                start_node_x=start[0],
                start_node_y=start[1],
                end_node_x=end[0],
                end_node_y=end[1],
                wall_pos=wall_pos,
            )
            execution_time, memory_usage = measure_memory_and_time(
                getattr(algo, method_name)
            )
            movements = (
                len(algo.route)
                if name != "Bidirectional"
                else len(algo.route_f) + len(algo.route_r)
            )
            data.append(
                {
                    "Algorithm": name,
                    "Runtime (s)": execution_time,
                    "Memory Usage (MB)": memory_usage,
                    "Movements": movements,
                    "Maze": image_name,
                }
            )

        all_data.extend(data)

    df = pd.DataFrame(all_data)
    df.to_excel(output_excel, index=False)
    print(f"Results saved to {output_excel}")


def main():
    parent_folder = "D:\\SV\\HK6\\Algorithms and Analysis\\Maze\\SourceImg\\Maze\\SquareMatrix\\5img\\caitienbangpriority"
    subdirs = next(os.walk(parent_folder))[1]
    for subdir in subdirs:
        subfolder_path = os.path.join(parent_folder, subdir)
        output_excel = os.path.join(parent_folder, f"{subdir}.xlsx")
        process_images_in_folder(subfolder_path, output_excel)
        gc.collect()


if __name__ == "__main__":
    main()
