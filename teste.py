import math

numero = -3
numer_jogos = 14
numero_convidados = 15

print(numero_convidados)

palavra1 = 'linguagem de programação'
palavra2 = 'Python'


print('Esta ', palavra1.capitalize(), ' se chama ', palavra2.upper())
print('Esta ', palavra1[0:9], ' se chama ', palavra2.upper())
print('Esta ', palavra1[9:], ' se chama ', palavra2.upper())
print('Esta ', palavra1[:9], ' se chama ', palavra2.upper())

n1 = 14
n2 = 6

print(f'Dividindo {n1} por {n2} o resultado é {n1 / n2}')
print(f'Somando {n1} por {n2} o resultado é {n1 + n2}')
print(f'O resto da divisão {n1} por {n2} o resultado é {n1 % n2}')
print(f'{n1} elevado {n2} o resultado é {n1**n2}')
print(f'A raiz quadrada de {n1} é {math.sqrt(n1)}')
print(f'A raiz quadrada de {n1} é {round(math.sqrt(n1), 2)}')

horas_gastas = float(input('Informe a quantiade de horas gastas na viagem: '))
velocidade_media = float(input('Informe a velocidade média na viagem: '))
distancia = horas_gastas * velocidade_media
litros_usados = distancia / 12.0
print('Foram gastos ', round(litros_usados, 2), ' litros na viagem')

# idade = input('Digite sua idade: ')
# print(idade)
