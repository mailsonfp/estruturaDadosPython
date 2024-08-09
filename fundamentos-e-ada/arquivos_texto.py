with open('frase1.txt', encoding="utf-8") as conteudo:
    for linha in conteudo:
        print(linha)

print('-' * 20)

with open('texto2.txt', 'w') as texto:
    texto.write('Nhaaaaaaiiiiinnnnnn mona, como a senhora tá?')

with open('texto2.txt', 'r') as tex:
    for linha in tex:
        print(linha)

# exercicio
print('-' * 20)

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('alunos.txt', 'w') as arquivo:
    for aluno, nota in alunos.items():
        arquivo.write(f'{aluno},{nota}\n')

with open('alunos.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
