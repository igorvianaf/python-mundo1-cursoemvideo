s = float(input('Informe o valor do seu salário: R$'))
a = s + (s * 15 / 100)
print(f'Parábens, seu salário aumentou, antes você recebia, \033[0;31;107m{s:.2f}\033[m,', end=' ')
print(f'agora receberá \033[0;32;107m{a:.2f}\033[m')
