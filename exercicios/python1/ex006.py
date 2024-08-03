from math import sqrt

numero = float(input('Digite um número: '))
print(f'O dobro de {numero} é {numero*2}, o triplo de {numero} é {numero*3}', end=',')
print(f'e a raiz quadrada de {numero} é {sqrt(numero):.2f}')
