import matplotlib.pyplot as plt

def plot_coordinates(coordinates):
    x_values = [coord[0] for coord in coordinates]
    y_values = [coord[1] for coord in coordinates]

    plt.scatter(x_values, y_values)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Coordinate Plot')
    plt.grid(True)
    plt.show()

# 用法示例
coordinates = [(1, 2), (3, 4), (5, 6)]  # 替换为您的坐标列表
plot_coordinates(coordinates)


