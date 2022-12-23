def kv_numbers(num):
    counter = 0
    while counter < num:
        yield counter ** 2
        counter += 1


kv_nums = kv_numbers(11)

for i in range(11):
    print(next(kv_nums))