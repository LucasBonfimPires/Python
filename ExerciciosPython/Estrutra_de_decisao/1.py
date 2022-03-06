#1. Faça um Programa que peça dois números e imprima o maior deles.

numeros = list()


for i in range(2):
    n1 = int(input('Informe 2 números: '))
    numeros.append(n1)
    
print('Os números informados foram: ', numeros)

if numeros[0] > numeros[1]:
    print(f'O maior número foi: {numeros[0]}')
if numeros[1] > numeros[0]:
    print(f'O maior número foi: {numeros[1]}')
