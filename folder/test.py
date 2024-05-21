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
        with open("binary_matrix.txt", "w") as file:
            for i in range(len(binary_matrix)):
                for j in range(len(binary_matrix[0])):
                    file.write(str(binary_matrix[i][j]))
                file.write("\n")

        print("a.txt")
        # result.append(binary_matrix)

        # Lưu tên của ảnh vào list
        image_names.append(os.path.splitext(os.path.basename(file_path))[0])

    return result, image_names  # Trả về kết quả và tên của các ảnh


def main():
    parent_folder = "D:\\SV\\HK6\\Algorithms and Analysis\\Maze\\SourceImg\\Maze\\Type\Test\\test1\\45_15"
    result, name = read_image(parent_folder)
    print(result)


if __name__ == "__main__":
    main()
