velocidade = float(input('Informe a velocidade do carro: '))
if velocidade > 80:
    print('O limite de velocidade é de 80km/h. Você ultrapassou esse limite.')
    print(f'Você foi multado em {(velocidade-80) * 7:.2f}')
else: print('Párabens, você está dentro do limite permitido')
