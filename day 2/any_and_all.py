list = [1, 2, 3, 4, 5, 0]
print(any(list))  # True
print(all(list))  # False

print('any([1, 1])', any([1, 1]))
print('all([1, 1])', all([1, 1]))

print()

print('any([1, 0])', any([1, 0]))
print('all([1, 0])', all([1, 0]))

print()

print('any([0, 0])', any([0, 0]))
print('all([0, 0])', all([0, 0]))
