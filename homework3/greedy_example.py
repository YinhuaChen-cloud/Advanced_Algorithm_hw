def greedy_load_balancing(tasks, servers):
    # 创建一个字典来跟踪每个服务器的负载
    server_loads = {server: 0 for server in servers}
    print(server_loads)

    # 遍历每个任务并将其分配给负载最低的服务器
    for task in tasks:
        # 找到当前负载最低的服务器
        min_load_server = min(server_loads, key=server_loads.get)
        # 将任务分配给该服务器
        server_loads[min_load_server] += task

    return server_loads

# 示例用法
tasks = [1, 2, 3, 4, 5, 6, 7]
servers = ['Server1', 'Server2', 'Server3']  # 服务器列表

result = greedy_load_balancing(tasks, servers)
print(result)

