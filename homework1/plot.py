import matplotlib.pyplot as plt

def plot_coordinates(coordinates):
    x_values = [coord[0] for coord in coordinates]
    y_values = [coord[1] for coord in coordinates]

    # 创建图形对象和坐标轴对象
    fig, ax = plt.subplots()

    ax.scatter(x_values, y_values)
    # 设置 x 和 y 轴的范围
    ax.set_xticks(range(-1, 12))
    ax.set_yticks(range(-1, 12))

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Coordinate Plot')
    plt.grid(True, which='both', linestyle='--')

    plt.show()

# Task1-1
# coordinates = [(5, 1), (6, 2), (7, 3), (6, 4), (5, 5), (4, 4), (3, 3), (4, 2)]
# coordinates = [(0, 4), (8, 3), (5, 1), (5, 10), (1, 5), (9, 8), (3, 1), (1, 9)]

# Task1-2
# coordinates = [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
coordinates = [(6, 1), (3, 7), (2, 7), (4, 2), (3, 4), (0, 5), (9, 2), (3, 2)]
plot_coordinates(coordinates)


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


