numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def kv(n):
    return n ** 2


kv_nums = list(map(kv, numbers))

print(kv_nums)

words = ['Hello', 'Python', 'Django']

counts = list(map(len, words))
print(counts)

# map with lambda

kub_numbers = list(map(lambda x: x ** 3, numbers))
print(kub_numbers)


# Caesar Cipher Algorithm

def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by

    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)

    return chr(rotated_pos - len(alphabet))


new_text = "".join(map(rotate_chr, "Nabiyev Fazliddin."))

print(new_text)
