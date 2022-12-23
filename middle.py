nums = [8, 50, 44, 42, 50, 16, 22, 31, 4, 92, 9, 62, 36, 96, 30, 58, 73]

nums_unique = list(dict.fromkeys(nums)) # dublicate qiymatlarni yo'qotadi

nums_unique.sort() # tartiblaydi

print(nums_unique[len(nums_unique)//2]) # tartiblangan royxatdagi listni ortasidagini qiymatni oladi