import re

texto = "Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e 11111-111 meu site é https://www.iaexpert.academy http://iaexpert.com.br"

print(re.findall(r'\d', texto))
print(re.findall(r'\d{5}-\d{3}', texto))
print(re.findall(r'https?://[A-Za-z0-9./]+', texto))