r1 = float(input('informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com esse comprimento de linha conseguimos formar um triângulo')
else:
    print('Com esse comprimento não conseguimos formar um triangulo')
