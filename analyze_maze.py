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


# Doc anh
def read_image(image_path):
    return


# Chon diem dau diem cuoi
def determind_start_end_point():
    return


def calculate_time_and_space_complexity(algorithm, image):
    start_time = time.time()
    start_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result = algorithm(image)
    end_time = time.time()
    end_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    execution_time = end_time - start_time
    memory_usage = end_memory_usage - start_memory_usage
    return execution_time, memory_usage


# def main():
#     image_path = "your_image_path.jpg"
#     image = read_image(image_path)

#     bfs = BFS()
#     dfs = DFS()
#     astar = AStar()
#     dijkstra = Dijkstra()
#     bidirectional = Bidirectional()

#     bfs_time, bfs_memory = calculate_time_and_space_complexity(bfs, image)
#     dfs_time, dfs_memory = calculate_time_and_space_complexity(dfs, image)
#     astar_time, astar_memory = calculate_time_and_space_complexity(astar, image)
#     dijkstra_time, dijkstra_memory = calculate_time_and_space_complexity(
#         dijkstra, image
#     )
#     bidirectional_time, bidirectional_memory = calculate_time_and_space_complexity(
#         bidirectional, image
#     )

#     print("BFS - Time:", bfs_time, "seconds, Memory:", bfs_memory, "bytes")
#     print("DFS - Time:", dfs_time, "seconds, Memory:", dfs_memory, "bytes")
#     print("A* - Time:", astar_time, "seconds, Memory:", astar_memory, "bytes")
#     print(
#         "Dijkstra - Time:", dijkstra_time, "seconds, Memory:", dijkstra_memory, "bytes"
#     )
#     print(
#         "Bidirectional - Time:",
#         bidirectional_time,
#         "seconds, Memory:",
#         bidirectional_memory,
#         "bytes",
#     )


if __name__ == "__main__":
    main()
