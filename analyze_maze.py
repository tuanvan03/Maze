from bfs_class import *
from dfs_class import *
from astar_class import *
from dijkstra_class import *
from bidirectional_class import *
import cv2
import time
import resource
from bfs_class import BFS
from dfs_class import DFS
from astar_class import AStar
from dijkstra_class import Dijkstra
from bidirectional_class import Bidirectional
from insert_maze import *
import os


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


def calculate_time_and_space_complexity(algorithm, image):
    start_time = time.time()
    start_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result = algorithm(image)
    end_time = time.time()
    end_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    execution_time = end_time - start_time
    memory_usage = end_memory_usage - start_memory_usage
    return execution_time, memory_usage


def main():
    image_path = "D:\\SV\\HK6\\Algorithms and Analysis\\Maze\\SourceImg\\Maze\\New"
    binary_img = read_image(image_path)

    for img in binary_img:
        start = (2, 0)
        end = (104, 58)


if __name__ == "__main__":
    main()
