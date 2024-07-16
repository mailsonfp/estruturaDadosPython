tupla = ("Beyonce", "Britney", "Gaga", "Rihanna")
print(tupla)
print('-' * 20)
print(tupla[3])
print('-' * 20)
for elemento in tupla:
    print(elemento)

print('-' * 20)

lista1 = ["Beyonce", "Britney", "Gaga", "Rihanna"]
lista2 = ["Madonna", "Kylie Minogue", "Whitney H.", "Celine Dion"]
lista3 = lista1 + lista2
for elemento in lista3:
    print(elemento)

lista4 = lista2 * 3
print('-' * 20)
print(lista4)

print('-' * 20)
print(lista3[2:6])

lista3.append("Tony Braxton")
print(lista3)

lista3.remove("Rihanna")

del lista4


