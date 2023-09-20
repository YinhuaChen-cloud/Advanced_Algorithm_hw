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
import itertools
import copy

# number of points
np = 8
# number of maps
nm = 4
# 用来写入图的文件
result_file = None
# x 坐标最小，最大
xmin = 0
xmax = 10
# y 坐标最小，最大
ymin = 0
ymax = 10

# 用来判断两个浮点数是否相等，在误差允许范围内 ------------ checked
def is_float_equal(a, b, epsilon=1e-5):
    return abs(a - b) < epsilon

# get the distance of two points -------------- checked
def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# greedy algorithm --------------------- checked
# 参数 start 表示起点的下标
# 返回 path, length，分别是路径和长度
def tsp_greedy(points, start):
    points_len = len(points)
    visited = [False] * points_len
    path = [start]  # 从start开始
    visited[start] = True
    path_len = 0

    while len(path) < points_len:
        current_point = path[-1]
        min_distance = math.inf
        next_point = None

        for i in range(points_len):
            if not visited[i]:

                print("current_point = " + str(current_point))
                print("points[current_point] = " + str(points[current_point]))
                print("points[i] = " + str(points[i]))

                distance = calculate_distance(points[current_point], points[i])
                if distance < min_distance:
                    min_distance = distance
                    next_point = i

        path.append(next_point)
        path_len += min_distance
        visited[next_point] = True

    print("path[-1] = " + str(path[-1]))
    print("points[start] = " + str(points[start]))

    path_len += calculate_distance(points[path[-1]], points[start])
    path.append(start)  # 回到起始城市

    return path, path_len

# 获取一个 TSP 解法的长度 -------------------- checked
def getPathLen(path):
    total_len = 0
    for i in range(len(path)):
        if i != len(path)-1:
            total_len += calculate_distance(path[i], path[i+1])
        else:
            total_len += calculate_distance(path[i], path[0])
    return total_len

# 获取点列表的最优路径和该路径长度 ----------------------- checked
# 返回最优解的 path 和 len
def getOptimal(points):
    # 首先获取 Points 的所有排列组合 
    # 以第一个城市为起点的所有排列组合实际上已经包括了所有的长度，所以这里可以直接除以 len(points)
    permutations = list(itertools.permutations(points))
    permutations = permutations[:len(permutations)//len(points)]

    min_len = math.inf
    min_path = None

    for path in permutations:
        path_len = getPathLen(path)
        if path_len < min_len:
            min_len = path_len
            min_path = path

    return min_path, min_len

# Judge whether a point list is qualified (所有点为起始点，跑贪婪算法都能出最优解) -------------- checked
def isQualify(points):
    # get the optimal solution
    optimal_path, optimal_len = getOptimal(points)
    # 以所有点为起点，跑贪婪算法
    count = 0
    for start in range(np):
        greedy_path, greedy_len = tsp_greedy(points, start)
        print("greedy_len = " + str(greedy_len))
        print("optimal_len = " + str(optimal_len))
        assert(is_float_equal(greedy_len, optimal_len) or greedy_len >= optimal_len)
        if is_float_equal(greedy_len, optimal_len):
            count += 1

    if count < len(points) and count > 0:
        # 打开文件，如果文件不存在则创建一个新文件，写入模式为追加模式
        global result_file
        result_file = open("result1-2.txt", "a")
        # 写入内容到文件
        result_file.write(str(points) + "\n")
        # 关闭文件
        result_file.close()

# ----------------------------------------- checked
def main():
    # 随机生成4幅图 (8个点)
    maps = []
    for _ in range(nm):
        points = []
        for _ in range(np):
            x = random.randint(xmin, xmax)
            y = random.randint(ymin, ymax)
            points.append((x, y))
        maps.append(points)

    # 进入一个死循环
    while(True):
        # 评估这四幅图里是否有符合要求的图 (所有点为起始点，跑贪婪算法都能出最优解)，若有，直接把符合要求的图 dump 出来，并继续
        for i in range(nm):
            isQualify(maps[i])            

        # 循环体，每幅图循环一次
        for i in range(nm):
            # 生成8个突变体(随机替换一个现存点为随机点)
            max_greedy_count = -1
            max_greedy_points = None

            for mutate_n in range(np):
                # 对 maps[i] 的深拷贝
                theMap = copy.deepcopy(maps[i]) 
                select_point = random.randint(0, np-1)
                x = random.randint(xmin, xmax)
                y = random.randint(ymin, ymax)
                theMap[select_point] = (x, y)
                # 使用暴力算法获取每个突变体的最优解
                optimal_path, optimal_len = getOptimal(theMap)
                # 使用贪婪算法，8个点都做一遍贪婪算法，计算有多少个起始点跑贪婪算法可以得到最优解
                greedy_count = 0
                for start in range(np):
                    greedy_path, greedy_len = tsp_greedy(theMap, start)
                    print("greedy_len = " + str(greedy_len))
                    print("optimal_len = " + str(optimal_len))
                    assert(is_float_equal(greedy_len, optimal_len) or greedy_len >= optimal_len)
                    if is_float_equal(greedy_len, optimal_len):
                        greedy_count += 1
                # 选择出最多起始点能跑出最优解的一个图
                # if max_greedy_count < greedy_count:
                if max_greedy_count < 1 and greedy_count > 0:
                    max_greedy_count = greedy_count
                    max_greedy_points = theMap
                elif greedy_count > 0 and max_greedy_count > greedy_count:
                    max_greedy_count = greedy_count
                    max_greedy_points = theMap
            
            # 用选择出的图替换掉当前图
            maps[i] = max_greedy_points

if __name__ == "__main__":
    main()

