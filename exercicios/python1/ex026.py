frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra a aparece:', frase.count('A'), 'vezes na frase')
print(f'A primeira letra A aparece na posição {frase.find('A')+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind('A')+1}')



## rfind - procure a partir do lado direito