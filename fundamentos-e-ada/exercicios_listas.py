import numpy as np

soma = 0
matriz = np.array([[3, 4, 1], [3, 1, 5]])
for linha in range(matriz.shape[0]):
    for coluna in range(matriz.shape[1]):
        soma += matriz[linha][coluna]

print(f'A soma dos elementos da matriz = {soma}')

print('-' * 20)

alunos = {}
for i in range(1, 4):
    nome = input('Informe o nome do aluno: ')
    nota = int(input('Informe a nota do aluno: '))
    alunos[nome] = nota

print(alunos)

somaNotas = 0
for nota in alunos.values():
    somaNotas += nota

print(f'A média das notas digitadas = {round(somaNotas/3, 2)}')

print('-' * 20)

lista = []
for i in range(1, 6):
    lista.append(int(input('Digite um número inteiro: ')))

print(lista)

soma = 0
for numero in lista:
    soma += numero

print(f'A soma dos números digitados = {soma}')
