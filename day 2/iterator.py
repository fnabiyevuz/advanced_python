"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

iter_list = iter(numbers)

print(iter_list.__next__())
print(next(iter_list))
print(iter_list.__next__())
print(next(iter_list))
print(iter_list.__next__())
print(next(iter_list))
print(iter_list.__next__())
print(next(iter_list))

try:
    print(next(iter_list))
except StopIteration:
    print("StopIteration")
"""


# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:

    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x


# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# Prints nothing
for i in Test(5):
    print(i)


class EvenNumbers:
    last = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.last += 2
        if self.last > 8:
            raise StopIteration
        return self.last


even_numbers = EvenNumbers()
for num in even_numbers:
    print(num)
