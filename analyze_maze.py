import os
import time
import pandas as pd
from PIL import Image
import numpy as np
import tracemalloc
import matplotlib.pyplot as plt
import seaborn as sns

from bfs_class import BreadthFirst
from settings import wall_nodes_coords_list

from bfs_class import *
from dfs_class import *
from astar_class import *
from dijkstra_class import *
from bidirectional_class import *
import openpyxl

def read_image(image_path):
    file_list = os.listdir(image_path)

    image_files = [
        os.path.join(image_path, file)
        for file in file_list
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))
    ]
    result = []
    image_names = []
    for file_path in image_files:
        img = Image.open(file_path)
        target_size = (104, 60)
        img_resized = img.resize(target_size, resample=Image.BILINEAR)
        matrix = np.array(img_resized)
        binary_matrix = (matrix[:, :, 0] > 128).astype(int)
        result.append(binary_matrix)
        image_names.append(os.path.splitext(os.path.basename(file_path))[0])
    return result, image_names

def measure_memory_and_time(execute_func):
    tracemalloc.start()
    start_time = time.time()
    execute_func()
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time = end_time - start_time
    memory_usage = peak / (1024**2)
    return execution_time, memory_usage

def main():
    image_path = "D:\\DaiHoc\\HK6\\TKDGTT\\Project\\Maze\\SourceImg\\Maze\\New\\thua"
    binary_img, image_names = read_image(image_path)
    count = 0
    # print(binary_img)
    all_data = []
    for matrix, image_name in zip(binary_img, image_names):
        print("Dang doc anh thu: ", count)
        count += 1
        data = []
        # print(matrix[2][0] )
        # print(matrix)
        for i in range(0,60,1):
            if (matrix[i][0] == 1):
                start = (2, i + 2)
                # print(i)
                break
            
        for i in range(59,0,-1):
            if (matrix[i][103] == 1):
                end = (105, i + 2)
                # print(i)
                break
        
        # print(start ,end)
        # start = (2, 5)
        # end = (105, 58)
        # print()
        wall_pos = wall_nodes_coords_list.copy()
        for j in range(104):
            for i in range(60):
                if matrix[i][j] == 0:
                    wall_pos.append((j + 2, i + 2))

        algorithms = [
            ("BFS", BreadthFirst),
            ("DFS", DepthFirst),
            ("A star", AStar),
            ("Dijkstra", Dijkstra),
            ("Bidirectional", Bidirectional),
        ]

        for name, AlgoClass in algorithms:
            algo = AlgoClass(app=None, start_node_x=start[0], start_node_y=start[1], end_node_x=end[0], end_node_y=end[1], wall_pos=wall_pos)
            execution_time, memory_usage = measure_memory_and_time(algo.execute)  # Updated to use execute method
            movements = len(algo.route) if name != "Bidirectional" else len(algo.route_f) + len(algo.route_r)
            data.append({
                "Algorithm": name,
                "Runtime (s)": execution_time,
                "Memory Usage (MB)": memory_usage,
                "Movements": movements,
                "Maze": image_name,
            })

        all_data.extend(data)
    
    df = pd.DataFrame(all_data)
    df.to_excel("big_maze.xlsx", index=False)

    # Vẽ biểu đồ
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=df, x='Maze', y='Runtime (s)', hue='Algorithm')
    plt.title('Runtime of Different Algorithms on Various Mazes')
    plt.xlabel('Maze')
    plt.ylabel('Runtime (s)')
    plt.legend(title='Algorithm')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
