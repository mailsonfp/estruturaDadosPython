import math
import datetime
import random
import time

print(f'Raiz quadrada de 32: {math.sqrt(32)}')
print(f'Seno de 32: {math.sin(32)}')
print(f'Cosseno de 32: {math.cos(32)}')
print(f'Log de 32 a base 4: {math.log(32, 4)}')
print(f'Log de 32 a base euler: {math.log(32)}')
print(f'pi: {math.pi}')

print('-' * 20)

print(datetime.date.today())
print(datetime.datetime.now())
data = datetime.date(2024, 7, 16)
print(data)

print('-' * 20)

print(random.randint(1,95698))
x = ['K', 'd', 13, '34-j', 'x']
print(random.choice(x))

print('-' * 20)

antes = time.time()
lista = []
for i in range(1, 100000000):
    lista.append(i)
depois = time.time()
print(f'Antes:  {antes} - Depois: {depois}')