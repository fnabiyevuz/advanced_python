"""
from copy import copy, deepcopy

li1 = [1, 2, [3, 5], 4]

print("li1 ID: ", id(li1), "Value: ", li1)
li2 = copy(li1)
print("li2 ID: ", id(li2), "Value: ", li2)
li3 = deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)

li1[2][0] = 0
print('Before a change')
print("li1 ID: ", id(li1), "Value: ", li1)
print("li2 ID: ", id(li2), "Value: ", li2)
print("li3 ID: ", id(li3), "Value: ", li3)
"""

a = [1, 2, 3, 4, 5]
b = list(a)

print(a, b)
# a.append('salom')
a[0] = "asl"

print(a, b)
