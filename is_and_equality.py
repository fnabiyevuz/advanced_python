a = 111
b = 111
c = a

d = 3000
e = 3000
f = d

print('a is b', a is b, 'id(a) =', id(a), 'id(b) =', id(b))
print('a == b', a == b, 'id(a) =', id(a), 'id(b) =', id(b))
print()
print('a is c', a is c, 'id(a) =', id(a), 'id(c) =', id(c))
print('a == c', a == c, 'id(a) =', id(a), 'id(c) =', id(c))
print()
print('d =', d, 'e =', e, 'd is e', d is e, 'id(d) =', id(d), 'id(e) =', id(e))
print('d =', d, 'e =', e, 'd == e', d == e, 'id(d) =', id(d), 'id(e) =', id(e))
print()
print('d =', d, 'f =', f, 'd is f', d is f, 'id(d) =', id(d), 'id(f) =', id(f))
print('d =', d, 'f =', f, 'd == f', d == f, 'id(d) =', id(d), 'id(f) =', id(f))
