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

m1 = float(input('Digite a nota M1: '))
m2 = float(input('Digite a nota M2: '))
m3 = float(input('Digite a nota M3: '))

media = (m1 + m2 + m3) / 3
print(media)

if 0.0 <= media <= 4.0:
    print('Aluno reprovado')
elif 4.1 <= media <= 6.0:
    exame = float(input('Digite a nota do exame'))
    if exame >= 6.0:
        print('Aprovado no exame')
    else:
        print('Reprovado no exame')
else:
    print('Aluno aprovado')
