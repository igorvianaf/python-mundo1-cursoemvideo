from random import shuffle

a = str(input('livro 1: '))
b = str(input('livro 2: '))
c = str(input('livro 3: '))
d = str(input('livro 4: '))
cores = {'azul': '\033[34m',
        'vermelho': '\033[31m',
        'roxo': '\033[35m',
        'cinza': '\033[37m',
        'limpa': '\033[m'}
lista = [a, b, c, d]
shuffle(lista)
print(f'A ordem de leitura será, ')
print('\033[34m', lista)
