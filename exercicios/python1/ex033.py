a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('informe o terceiro número: '))
##verificando quem é menor
menor = a
if b<a and b<c:
 menor = b
if c<a and c<b:
  menor = c
print(f'Menor valor {menor}')
maior = a
if b>a and b>c:
 maior = b
if c>a and c>b:
 maior = c
 print(f'Maior valor {maior}')