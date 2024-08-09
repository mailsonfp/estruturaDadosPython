class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            return 'não é um triângulo'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
            return 'triângulo isósceles'
        else:
            return 'outro tipo de triângulo'


t1 = Triangulo(5, 1, 3, 4, 3)
print(t1.lado1)
print(f't1.area = {t1.area()}')
print(f't1.tipo = {t1.tipo()}')

t2 = Triangulo(8, 8, 8, 16, 9)
print(f't1.area = {t2.area()}')
print(f't1.tipo = {t2.tipo()}')
