distancia = float(input('Qual a distania da viagem em KM: '))
if distancia <= 200:
    print(f'O preço da passagem será: R$ {distancia * 0.5:.2f}')
else:
    print(f'O preço da passagem será: R$ {distancia * 0.45:.2f}')
