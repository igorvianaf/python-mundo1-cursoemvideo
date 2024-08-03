from random import randint
from time import sleep

n = randint(1,5)
print('O computador está escolhendo um número')
print('PROCESSANDO...')
sleep(3)
print('Número escolhido!')
escolha = int(input('O computador escolheu um número entre 0 e 5, tente adivinhar: '))
if escolha == n:
    print(f'Eu pensei no {n}. Parabéns, você acertou! 🥳🥳')
else:
    print(f'Eu pensei no número {n}. Você perdeu! 😵😵')
