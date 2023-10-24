def split_list(lst, n):
    if n == 1:
        yield [lst]
        return

    for i in range(1, len(lst) - n + 2):
        for rest in split_list(lst[i:], n - 1):
            yield [lst[:i]] + rest

my_list = [1, 2, 3, 4, 5]
result = list(split_list(my_list, 3))
print(result)

