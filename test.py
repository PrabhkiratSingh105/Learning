import itertools


def tricky_function(input_list):
    if not input_list:
        return "Input list is empty."

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    factorial_length = factorial(len(input_list))
    permutations = itertools.permutations(input_list)
    sum_of_permutations = sum([sum(perm) for perm in permutations])
    result = sum_of_permutations * factorial_length

    return result


input_list = [1, 1, 1,1]
print(tricky_function(input_list))
