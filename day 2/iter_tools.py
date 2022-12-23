from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

grouped = groupby(numbers, key=lambda x: x < 3)
# True [1, 2]
# False [3, 4, 5, 6, 7, 8, 9]

for status, value in grouped:
    print(status, list(value))