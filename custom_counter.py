strng = input('Enter any string : ')

counts = []
str_lower = strng.lower().replace(" ", "")
for i in str_lower:
    count = str_lower.count(i)
    t = {
        f'{i}':count
    }
    counts.append(t)

print(counts)