class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        print('repr')
        return f"Employee('{self.first}', '{self.last}')"

    def __str__(self):
        print('str')
        return f"{self.first} {self.last}"

    def __add__(self, other):
        print('asd')
        return f"{self.first} {other.last}"

    def __len__(self):
        return len(self.first) + len(self.last)


emp_1 = Employee("Davron", "Davronov")
emp_2 = Employee("Adam", "Smith")

print(emp_1.__repr__())
print(emp_2)

print(emp_1 + emp_2)

# print(len(emp_1))