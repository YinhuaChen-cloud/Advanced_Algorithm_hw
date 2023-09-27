import matplotlib.pyplot as plt

def plot_coordinates(coordinates, optimalPath, worse_path):
    x_values = [coord[0] for coord in coordinates]
    y_values = [coord[1] for coord in coordinates]

    # 创建图形对象和坐标轴对象
    fig, ax = plt.subplots()

    ax.scatter(x_values, y_values)
    # 设置 x 和 y 轴的范围
    ax.set_xticks(range(-1, 31))
    ax.set_yticks(range(-1, 31))

    # 绘制线
    path_x_values = [coord[0] for coord in optimalPath]
    path_y_values = [coord[1] for coord in optimalPath]
    ax.plot(path_x_values, path_y_values, color='blue', label='line')

    path_x_values = [coord[0] for coord in worse_path]
    path_y_values = [coord[1] for coord in worse_path]
    # for i in range(len(path_x_values) - 1 ):
        # ax.arrow(path_x_values[i], path_y_values[i], path_x_values[i+1]-path_x_values[i], path_y_values[i+1]-path_y_values[i], head_width=0.5, head_length=0.5, fc='red', ec='red', linestyle="dashed")
    ax.plot(path_x_values, path_y_values, color='red', label='line', linestyle="dashed")
  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Coordinate Plot (ratio: 1.7941772473604027)')
    plt.grid(True, which='both', linestyle='--')

    plt.show()

# Task1-1
# coordinates = [(5, 1), (6, 2), (7, 3), (6, 4), (5, 5), (4, 4), (3, 3), (4, 2)]
# coordinates = [(0, 4), (8, 3), (5, 1), (5, 10), (1, 5), (9, 8), (3, 1), (1, 9)]

# Task1-2
# coordinates = [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
# coordinates = [(6, 1), (3, 7), (2, 7), (4, 2), (3, 4), (0, 5), (9, 2), (3, 2)]

# Task1-3
# coordinates = [(4, 4), (4, 6), (6, 6), (6, 4), (5, 9), (5, 1), (1, 5), (9, 5)]
# optimal_path = ((4, 4), (1, 5), (4, 6), (5, 9), (6, 6), (9, 5), (6, 4), (5, 1), (4, 4))

# Task1-4
# coordinates = [(0, 4), (8, 3), (5, 3), (5, 10), (1, 5), (9, 8), (1, 9)]
# optimal_path = ((1, 5), (0, 4), (5, 3), (8, 3), (9, 8), (5, 10), (1, 9), (1, 5))
# worse_path = ((1, 5), (0, 4), (1, 9), (5, 10), (9, 8), (8, 3), (5, 3), (1, 5))

# Task2-1
coordinates = [(3, 12), (16, 24), (6, 3), (1, 4), (18, 12), (26, 29), (10, 6), (24, 19), (9, 17)]
optimal_path = ((3, 12), (1, 4), (6, 3), (10, 6), (18, 12), (24, 19), (26, 29), (16, 24), (9, 17), (3, 12))
worse_path_indices = [2, 6, 0, 8, 1, 7, 4, 3, 5, 2]
worse_path = [coordinates[i] for i in worse_path_indices ] 

plot_coordinates(coordinates, optimal_path, worse_path)


# 用法示例
# coordinates = [(1, 2), (3, 4), (5, 6)]  # 替换为您的坐标列表

# def plot_coordinates(coordinates):
#     x_values = [coord[0] for coord in coordinates]
#     y_values = [coord[1] for coord in coordinates]
# 
#     plt.scatter(x_values, y_values)
#     # 设置 x 和 y 轴的范围
#     plt.xlim(-1, 11)
#     plt.ylim(-1, 11)
# 
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Coordinate Plot')
#     plt.grid(True, which='both', linestyle='--')
# 
#     plt.show()


