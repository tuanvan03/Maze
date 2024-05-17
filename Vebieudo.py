import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel
df = pd.read_excel('C:\\Daihoc\\Ky2nam3\\TK_DGTT\\Baitaplon\\Maze\\Small_maze_data.xlsx')

# Lọc dữ liệu cho từng thuật toán
bfs_data = df[df['Name algorithm'] == 'BFS']
dfs_data = df[df['Name algorithm'] == 'DFS']
astar_data = df[df['Name algorithm'] == 'AStar']
dijkstra_data = df[df['Name algorithm'] == 'Dijkstra']
bidirectional_data = df[df['Name algorithm'] == 'Bidirectional']

# Vẽ biểu đồ đường
plt.figure(figsize=(10, 6))

# Vẽ đường cho BFS
plt.plot(bfs_data['Maze'], bfs_data['Runtime (s)'], label='BFS')

# Vẽ đường cho DFS
plt.plot(dfs_data['Maze'], dfs_data['Runtime (s)'], label='DFS')

# Vẽ đường cho AStar
plt.plot(astar_data['Maze'], astar_data['Runtime (s)'], label='AStar')

# Vẽ đường cho Dijkstra
plt.plot(dijkstra_data['Maze'], dijkstra_data['Runtime (s)'], label='Dijkstra')

# Vẽ đường cho Bidirectional
plt.plot(bidirectional_data['Maze'], bidirectional_data['Runtime (s)'], label='Bidirectional')

# Đặt tên trục x
plt.xlabel('Maze')

# Đặt tên trục y
plt.ylabel('Runtime (s)')

# Đặt tiêu đề cho biểu đồ
plt.title('Comparison of Algorithm Runtimes')

# Đặt chú thích cho biểu đồ
plt.legend()

# Hiển thị biểu đồ
plt.show()
