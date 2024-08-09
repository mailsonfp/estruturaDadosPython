coleta = {'aedes': 32, 'aedes albopictus': 22, 'anopheles': 14}

print(coleta['aedes'])

coleta['rhodnius'] = 11

print(coleta['rhodnius'])

del(coleta)['rhodnius']

print(coleta.items())
print(coleta.keys())
print(coleta.values())

coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
print(coleta2)

coleta.update(coleta2)
print(coleta)

for especie, num_especies in coleta.items():
    print(f'Espécie: {especie}, quantidade: {num_especies}')

biomeleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo',
                'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')

print('-' * 20)
print(biomeleculas)

conjunto = set(biomeleculas)

print(conjunto)

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)

print('-' * 20)
print(c3)

print(c1.difference(c2))
print(c2.difference(c1))
