n = int(input('Digite um número para saber se é par ou ímpar: '))
resultado = n % 2
if resultado == 1:
    print(f'{n} é um número ímpar')
else:
    print(f'{n} é um número par')
