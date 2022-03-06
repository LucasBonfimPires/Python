# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.M

while True:
    letras = str(input('Informe seu sexo: [M] - Masculino / [F] - Feminino: '))
    if letras == 'F' or letras == 'f': print('Mulher')
    elif letras == 'M' or letras == 'm': print('Homem')
    elif letras != 'M' or letras != 'F' or letras != 'm' or letras != 'f': print('Sexo inválido')
