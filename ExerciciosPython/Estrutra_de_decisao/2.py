#2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numeros = []

for i in range(2):
    n1 = int(input('Informe 2 números, positivos ou negativos: '))
    numeros.append(n1)
print(f'Os números informados foram: {numeros}')

if numeros[0] < 0:
    print(numeros[0])
if numeros[1] < 0:
    print(numeros[1])