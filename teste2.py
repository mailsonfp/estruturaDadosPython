a = True
b = False

print(a == b)
print(a and b)
print(a & b)

c = a and b

print(b and c)
print(not (b and c))

if not (b and c):
    print('É isso ai parça')
else:
    print('deu ruim!')