import re

frase = 'Olá, meu número de telefone é (42)00010-0000'
print(re.search(r'\(\d{2}\)\d{4,5}-\d{4}', frase))

frase = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
print(re.search(r'[A-Za-z]{3}-\d{4}', frase))

email = 'Entre em contato, meu email é teste@teste.com'
print(re.search(r'\w+@\w+\.com', email))

# re.match identifica a ocorrênciia no começo da string
frase = 'A placa de carro que eu anotei durante a batida foi FRT-1998'
print(re.match(r'[A-Za-z]{3}-\d{4}', frase))

emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''
print(re.findall(r'\w+@\w+\.\w*', emails))
print(re.findall(r'\w+@\w+\.\w*', emails))
print(re.findall(r'\w+@\w+\.\w*', emails))
