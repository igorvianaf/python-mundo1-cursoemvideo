salario = float(input('Qual o valor do seu salário? '))
if salario > 1250:
    print(f'Parábens, seu salário teve um aumento e agora é {salario+(salario*10/100)}')
else:
    print(f'Seu salário teve um aumento de 15%, agora você receberá {salario+(salario*15/100)}')
