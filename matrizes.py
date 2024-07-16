import numpy as np

matriz = np.array([[2, 3, 1], [4, 5, 7]])
print(matriz)

print('-' * 20)
print(matriz[0])

print('-' * 20)
print(matriz.shape)

print('-' * 20)
print(matriz[1])

print('-' * 20)
print(matriz[1][2])

print('-' * 20)
for linha in range(matriz.shape[0]):
    print(matriz[linha])
    for coluna in range(matriz.shape[1]):
        print(matriz[linha][coluna])

