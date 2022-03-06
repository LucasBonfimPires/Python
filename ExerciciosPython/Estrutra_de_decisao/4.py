#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

while True:
    vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    letra = str(input('Informe uma letra do alfabeto brasileiro: '))

    if letra in vogais:
        print('Vogal')
    else:
        print('Consoante')