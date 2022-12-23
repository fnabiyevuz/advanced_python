from functools import reduce


def my_add(a, b):
    return a + b


numbers = [0, 1, 2, 3, 4]

result = reduce(my_add, numbers)

print(result)

# with lambda

result = reduce(lambda x, y: x + y, numbers)

print(result)
