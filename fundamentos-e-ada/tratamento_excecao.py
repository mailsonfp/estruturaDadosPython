while True:
    try:
        n = int(input('Digite um número inteiro: '))
    except:
        print('Valor inválido')
    else:
        print(f'Valor digitado é {n}')
        break

while True:
    try:
        p = int(input('Digite um número inteiro'))
    except ValueError:
        print('Valor inválido')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução')
        break
    else:
        print(f'Valor digitado é {p}')
        break

# exercicio
lista = []
try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))
    divisao = lista[0] / lista[1]
except ValueError:
    print('Erro! Valor inválido')
except ZeroDivisionError:
    print('Erro! Divisão por zero')
except IndexError:
    print('Erro! Índice inválido')
except KeyboardInterrupt:
    print('Usuário interrompeu a execução')
else:
    print(f'A divisão é {divisao}')
