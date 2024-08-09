def le_valores():
    tempo_digitado = float(input('Informe a quantidade de horas gastas: '))
    velocidade = float(input('Informe a velocidade média: '))
    return tempo_digitado, velocidade

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade


def calcula_litros(distancia):
  return distancia / 12

def imprime(velocidade, tempo, distancia, litros):
  print('Velocidade:', velocidade)
  print('Tempo:', tempo)
  print('Distância:', distancia)
  print('Litros:', litros)


tempo, velocidade_media = le_valores()
distancia = calcula_distancia(velocidade_media, velocidade_media)
litros = calcula_litros(distancia)
imprime(velocidade_media, tempo, distancia, litros)

def converte_grau(graus_celsius):
    return (9 * graus_celsius + 160) / 5


def ler_grau():
    return float(input('Informe a temperatura em grau Celsius: '))


def imprime_resultado(graus_fahrenheit):
    print(f'A temperatura correspondente em fahrenheit é: {graus_fahrenheit}')


graus_celsius = ler_grau()
graus_fahrenheit = converte_grau(graus_celsius)
imprime_resultado(graus_fahrenheit)