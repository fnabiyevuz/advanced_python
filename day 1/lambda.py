def kvadrat(x):
    return x ** 2

print("Funksiyadan qaytgan qiymat : ", kvadrat(8))

kvadrat_lambda = lambda x: x ** 2
print("Lambda funksiyadan qaytgan qiymat : ", kvadrat_lambda(7))

full_name = lambda first, last: f"Fullname: {first} {last}"
print(("Fazliddin", "Nabiyev"))

print((lambda x, y: x ** y)(2, 5))

high_ord_func = lambda x, func: x + func(x)
result = high_ord_func(2, lambda x: x * x)
# result = high_ord_func(2, lambda x: x + 3)
print(result)

f = lambda a=2, b=3: lambda c: a + b + c
o = f()
print(o(6))

square = lambda x: x ** 2
product = lambda f, n: lambda x: f(x) * n

ans = product(square, 2)(10)
print(ans)

