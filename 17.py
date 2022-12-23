dict = [
    {'son' : 1}, 
    {'son' : 2}, 
    {'son' : 3}, 
    {'son' : 4}, 
    {'son' : 5}, 
    {'son' : 6}, 
    {'son' : 7}, 
    {'son' : 8}
]


juft = 0
toq = 0
for i in dict:
    if i['son'] % 2 == 0:
        juft += 1
    else:
        toq += 1

print('juft=',juft)
print('toq=',toq)

# universitet = [
#     {'kurator': 'Anvar Narzullayev',
#   'kurs:': 1,
#   'talabalar': [{'familiya': 'Jaloldinov',
#                               'ism': 'Xayrullo',
#                               'manzil': 'Asaka',
#                               'yosh': 20},
#                 {'familiya': 'Abdunabiyev',
#                               'ism': 'Shohruh',
#                               'manzil': 'Buloqboshi',
#                               'yosh': 17},
#                 {'familiya': 'Arobboyev',
#                               'ism': 'Javohir',
#                               'manzil': 'Marhamat',
#                               'yosh': 18},
#                 {'familiya': 'Nabiyev',
#                               'ism': 'Fazliddin',
#                               'manzil': 'Shaxrixon',
#                               'yosh': 19},
#                 {'familiya': 'Nuriddinov',
#                               'ism': 'Umidjon',
#                               'manzil': 'Jalaquduq',
#                               'yosh': 16},
#                 {'familiya': 'Malikov',
#                               'ism': 'Fayzullo',
#                               'manzil': 'Baliqchi',
#                               'yosh': 17}]},
#  {'kurator': 'Nabijonov Doniyor',
#   'kurs:': 1,
#   'talabalar': [{'familiya': 'Xursanov',
#                               'ism': 'Odiljon',
#                               'manzil': 'Paxtaobod',
#                               'yosh': 20},
#                 {'familiya': 'Sobirov',
#                               'ism': 'Sardor',
#                               'manzil': 'Izboskan',
#                               'yosh': 16},
#                 {'familiya': 'Sherzod',
#                               'ism': 'Aliyev',
#                               'manzil': 'Marhamat',
#                               'yosh': 19},
#                 {'familiya': 'Nabijon',
#                               'ism': 'Jorayev',
#                               'manzil': 'Oltinkol',
#                               'yosh': 18},
#                 {'familiya': 'Ibrohimov',
#                               'ism': 'Shohjahon',
#                               'manzil': 'Andijon shahar',
#                               'yosh': 21},
#                 {'familiya': 'Jumanov',
#                               'ism': 'Sirojiddin',
#                               'manzil': 'Baliqchi',
#                               'yosh': 17}]}]

# counter = 0
# for group in universitet:
#     for talaba in group['talabalar']:
#         if talaba['yosh'] > 17:
#             counter += 1
# print(counter)

# # def solution(sequence):
# #     k = i = 0
# #     while i < len(sequence)-1:
# #         if sequence[i] >= sequence[i+1]:
# #             k += 1
# #             sequence.pop(i+1)
# #             i=0
# #             if k > 1:
# #                 return False
# #             continue
# #         i+=1
# #     return True

# # print(solution([1, 2, 3, 4, 3, 6]))