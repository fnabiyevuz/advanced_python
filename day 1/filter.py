def odd(num):
    if num % 2 == 1:
        return True
    else:
        return False


def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = list(filter(odd, numbers))
even_numbers = list(filter(even, numbers))
print(odd_numbers)
print(even_numbers)

# filter with lambda

odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(odd_numbers)
print(even_numbers)
