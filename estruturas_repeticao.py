for numero in range(1, 6):
    print(numero)

print('-' * 20)

for numero in range(6, 0, -1):
    print(numero)

print('-' * 20)

palavra = 'Mona, cê é maluca?'
for letra in palavra:
    print(letra)

print('-' * 20)

tamanho = len(palavra)
numero = 1
while numero < tamanho:
    print(palavra[numero])
    numero += 1

numero = 1
somaNotas = 0
while numero < 6:
    somaNotas += int(input(f'Digite a nota número {numero}: '))
    numero += 1

print(f'A média das notas é {somaNotas/5}')

for numero in range(1, 11):
    print(f'3 x {numero} = {3 * numero}')

print('-' * 20)

for numero in range(1, 11):
    print('7 x {} = {}'.format(numero, numero * 7))
