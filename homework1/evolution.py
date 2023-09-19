# 综合来说，我们需要一个进化算法，流程如下：
# 
# 随机生成8个点 (4幅图)
# 进入一个死循环
#     评估这四幅图里是否有符合要求的图（所有点为起始点，跑贪婪算法都能出最优解），若有，直接把符合要求的图 dump 出来，并继续
#     循环体，每幅图循环一次
#         生成8个突变体(随机替换一个现存点为随机点)
#         使用暴力算法获取每个突变体的最优解
#         使用贪婪算法，8个点都做一遍贪婪算法，计算有多少个起始点跑贪婪算法可以得到最优解
#         选择出最多起始点能跑出最优解的一个图，替换掉当前图

import random
import math

# number of points
np = 8
# number of maps
nm = 4

# get the distance of two points
def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# greedy algorithm
def tsp_greedy(points):
    points_len = len(points)
    visited = [False] * points_len
    path = [0]  # 从第一个城市开始
    visited[0] = True

    while len(path) < num_cities:
        current_city = path[-1]
        min_distance = math.inf
        next_city = None

        for i in range(num_cities):
            if not visited[i]:
                distance = calculate_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city = i

        path.append(next_city)
        visited[next_city] = True

    path.append(0)  # 回到起始城市
    return path

# 示例用法
cities = [(0, 0), (1, 2), (3, 1), (2, 3), (1, 1)]
optimal_path = tsp_greedy(cities)
print(optimal_path)



def getOptimal(points):
    

# Judge whether a point list is qualified (所有点为起始点，跑贪婪算法都能出最优解)
def isQualify(points):
    # get the optimal solution
    getOptimal(points)

def main():
    # 随机生成4幅图 (8个点)
    maps = []
    for _ in range(nm):
        points = []
        for _ in range(np):
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            points.append((x, y))
        maps.append(points)

    # 进入一个死循环
    while(True):
        # 评估这四幅图里是否有符合要求的图 (所有点为起始点，跑贪婪算法都能出最优解)，若有，直接把符合要求的图 dump 出来，并继续
        for i in range(nm):
            isQualify(maps[i])            

        exit(0)
#     循环体，每幅图循环一次
#         生成8个突变体(随机替换一个现存点为随机点)
#         使用暴力算法获取每个突变体的最优解
#         使用贪婪算法，8个点都做一遍贪婪算法，计算有多少个起始点跑贪婪算法可以得到最优解
#         选择出最多起始点能跑出最优解的一个图，替换掉当前图

if __name__ == "__main__":
    main()

