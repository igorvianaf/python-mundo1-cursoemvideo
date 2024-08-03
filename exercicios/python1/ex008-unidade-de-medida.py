m = float(input('Informe uma valor em metro: '))
dm = m*10
c = m*100
mm = m*1000
dam = m/10
hm = m/100
km = m/1000
print(f'{m:.1f} metros equivale a {dm:.1f} decimetros, {c:.1f} centímetros, {mm:.1f} milimetros', end=', ')
print(f'{dam:.1f} decametros, {hm:.1f} hectometro {km:.5f} kilometros')
