l = float(input('Informe a largura da parede em metros: '))
a = float(input('Agora, informe a altura da parede em metros: '))
area = l*a
q = area*0.5
print(f'Para uma parede com largura de {l}m, altura de {a}m e área de {area:.1f}m²', end=' ')
print(f'é necessário {q:.1f}l de tinta')
