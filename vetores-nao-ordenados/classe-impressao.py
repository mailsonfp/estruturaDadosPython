import numpy
import numpy as np


class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def print(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insert(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida, Márcia!')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def search(self, value):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == value:
                return i

        return -1

    def remove(self, value):
        value_index = self.search(value)
        if vector.search(value) < 0:
            print('Errrrrroooooou')
            return
        else:
            for i in range(value_index, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1


if __name__ == '__main__':
    vector = VetorNaoOrdenado(5)
    vector.print()
    vector.insert(24)
    vector.insert(35)
    vector.insert(58)
    vector.insert(10)
    vector.insert(11)
    vector.print()
    vector.insert(110)
    if vector.search(24) >= 0:
        print('Acertou miseravi!')

    if vector.search(110) < 0:
        print('Errrrrroooooou!')

    vector.remove(110)
    vector.remove(58)
    vector.print()