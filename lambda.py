"""
from datetime import datetime 
# kv = lambda x, a, b, c: a*x**2+b*x + c

# print(kv(3, 1,2,3))
time1 = datetime.now()

print(list(map(lambda x : x**2, range(1, 10001))))

time2 = datetime.now()

li = []
for i in range(1, 10001):
    li.append(i**2)
print(li)

time3 = datetime.now()

print(list(filter(lambda x : x%2==0, range(1, 10001))))

time4 = datetime.now()

print('map time : ', time2-time1)
print('for time : ', time3-time2)
print('filter time : ', time4-time3)
# print('for time / map time : ', (time3-time2).microseconds / (time2-time1).microseconds )




f = map(int, ['1','2', '3'])

for i in f:
    print(i)

c = map(str, f)

print(list(c))


from functools import reduce

pro = reduce(lambda x,y,z: x+y+z, range(1, 10))

print(pro)

from collections import Counter

words = [
    [2001, 2023],
    [2002, 2024],
    [2003, 2025],
    [2004, 2026],
    [2005, 2027],
    [2006, 2028]
]

min = 2001
max = 2028

pointer = 2012

uniq = []

# for y in range(min, max):
#     if w[0] < pointer and w[1] > pointer:


a = 'asdasd'
b = list(a)

print(b)

from collections import namedtuple

Point = namedtuple('Point', 'x, y')
print(Point)

a = Point(1,3)

print(a)
"""
from collections import defaultdict, deque

d = deque([], maxlen=5)

for i in range(1,10):
    d.append(i)

print(d)
d.rotate()
print(d)