from itertools import permutations

def split_list(lst, n):
    if n == 1:
        yield [lst]
        return

    for i in range(1, len(lst) - n + 2):
        for rest in split_list(lst[i:], n - 1):
            yield [lst[:i]] + rest

def get_permutations(lst):
    return list(permutations(lst))

def getMakeSpan(list):
    max = 0
    for machine in list:
        sum = 0
        for load in machine:
            sum += load
        if(max < sum):
            max = sum
    return max

def greedy_load_balancing(tasks, m):
    servers = ["Server" + str(i) for i in range(1, m+1)]
    # 创建一个字典来跟踪每个服务器的负载
    server_loads = {server: 0 for server in servers}

    # 遍历每个任务并将其分配给负载最低的服务器
    for task in tasks:
        # 找到当前负载最低的服务器
        min_load_server = min(server_loads, key=server_loads.get)
        # 将任务分配给该服务器
        server_loads[min_load_server] += task

    maxserver = max(server_loads, key=server_loads.get)
    makespan = server_loads[maxserver]

    return makespan

# get the optimal solution and the worstGreedy solution
def getOptimalAndWorst(m, jobs):
    # 1. get all permutations of jobs
    all_perm = get_permutations(jobs)
    # the result is a list of tuples
    # 2. get all possible split, and get the optimal and optimalSolution
    optimal = float('inf')
    optimalSolution = None
    for atuple in all_perm:
        alist = list(atuple)
        all_list = list(split_list(alist, m))
        # get optimal and optimalSolution
        for item in all_list:
            makespan = getMakeSpan(item)
            if(optimal > makespan):
                optimal = makespan
                optimalSolution = item
        print(all_list)
    # 3. get the worstGreedy and worstGreedySolution (greedy)
    worstGreedy = 0
    worstGreedySolution = None
    bestGreedy = float('inf')
    bestGreedySolution = None
    for atuple in all_perm:
        tasks = list(atuple)
        makespan = greedy_load_balancing(tasks, m)
        if(worstGreedy < makespan):
            worstGreedy = makespan
            worstGreedySolution = tasks
        if(bestGreedy > makespan):
            bestGreedy = makespan
            bestGreedySolution = tasks

    return optimal, optimalSolution, worstGreedy, worstGreedySolution, bestGreedy, bestGreedySolution

# number of machines
m = 4
# jobs list
jobs = [1, 1, 1, 1, 1, 1, 1,4]
# get the optimal solution and the worstGreedy solution
optimal, optimalSolution, worstGreedy, worstGreedySolution, bestGreedy, bestGreedySolution = getOptimalAndWorst(m, jobs)
# print the result
print("optimal = {}, optimalSolution = {}".format(optimal, optimalSolution))
print("worstGreedy = {}, worstGreedySolution = {}".format(worstGreedy, worstGreedySolution))
print("bestGreedy = {}, bestGreedySolution = {}".format(bestGreedy, bestGreedySolution))

