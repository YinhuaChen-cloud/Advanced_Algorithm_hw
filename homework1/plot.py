import matplotlib.pyplot as plt

def plot_coordinates(coordinates):
    x_values = [coord[0] for coord in coordinates]
    y_values = [coord[1] for coord in coordinates]

    # 创建图形对象和坐标轴对象
    fig, ax = plt.subplots()

    ax.scatter(x_values, y_values)
    # 设置 x 和 y 轴的范围
    ax.set_xticks(range(-1, 11))
    ax.set_yticks(range(-1, 11))

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Coordinate Plot')
    plt.grid(True, which='both', linestyle='--')

    plt.show()


# 用法示例
# coordinates = [(1, 2), (3, 4), (5, 6)]  # 替换为您的坐标列表
coordinates = [(7, 9), (9, 3), (8, 6), (1, 0), (0, 5), (7, 9), (0, 10), (3, 10)]
plot_coordinates(coordinates)

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


