from math import hypot

coposto = float(input('Informe o comprimento do cateto oposto: '))
cadjacente = float(input('Informe o comprimento do cateto adjacente: '))
hi = hypot(coposto, cadjacente)
print(f'O comprimento da hipotenusa é: {hi:.2f} ')
## certo!!!
