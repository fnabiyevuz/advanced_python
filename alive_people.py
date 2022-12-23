# data = [
#     [1972, 2010],
#     [1973, 2011],
#     [1974, 2012],
#     [1975, 2008],
#     [1970, 2006],
#     [1977, 2022],
#     [1978, 2016],
#     [1978, 2019],
#     [2020, 2022],
#     [2021, 2024],
#     [2021, 2025],
# ]
from collections import Counter
data = [(1920, 1939), (1911, 1944), (1920, 1955), (1938, 1939)]
new_list=[]
def alive_people(data:list)->dict:
    
    for d in data:

        new_list.extend(list(range(d[0], d[1]+1)))

    new_list

    return Counter(new_list).most_common(1)
    

print(alive_people(data))
# def alive_people(data:list)->dict:

#     birth = list(map(lambda d: d[0], data))
#     birth_unique = list(dict.fromkeys(birth))
#     maxi = 0
#     for b in birth_unique:
#         count = 0
#         for d in data:
#             if d[0] <= b and b <= d[1]:
#                 count += 1
#         if maxi < count:
#             maxi = count
#             result = {
#                 'year':b,
#                 'alive_people':count
#             }
#     return result

# print(alive_people(data))