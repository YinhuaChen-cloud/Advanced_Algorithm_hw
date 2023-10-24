from itertools import permutations

def get_permutations(lst):
    return list(permutations(lst))

# Example usage
my_list = [1, 2, 3]
permutations_list = get_permutations(my_list)
print(permutations_list)

