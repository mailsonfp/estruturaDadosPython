def mensagem():
    print('Hi Lorena!')


def mensagem_parametro(nome):
    print(f'Hi {nome}!')


def soma(a, b):
    return a + b


def calcula_energia_potecial_gravitacional(m, h, g = 10):
    e = g * m * h
    return e


mensagem()
mensagem_parametro('Lorena')
resultado = soma(55,66)
print(resultado)
resultado = calcula_energia_potecial_gravitacional(30, 12)
print(resultado)
resultado = calcula_energia_potecial_gravitacional(30, 12, 9.8)
print(resultado)
