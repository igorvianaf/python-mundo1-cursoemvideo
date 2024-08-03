from math import radians, sin, cos, tan

num = float(input('Informe o ângulo para saber o seno, conseno e tangente: '))
sen = sin((radians(num)))
cos = cos(radians(num))
tang = tan(radians(num))
print(f'Para o ângulo {num}º, o seno é {sen:.2f}, o coseno é {cos:.2f} e a tangente é {tang:.2f}')
##certoo!!!