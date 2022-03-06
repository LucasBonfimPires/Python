# 5. Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

count = 1
media = []
for i in range(2):
    nota = float(input(f'Informe a nota  {count} do aluno : '))
    media.append(nota)
    
    count += 1
    
media_final = (media[0] + media[1]) / 2

if media_final >= 7  and media_final < 10:
    print(f'Aprovado, nota: {media_final}')
elif media_final == 10:
    print(f'Aprovado com Distinção, nota: {media_final}')
elif media_final < 7:
    print(f'Reprovado, nota: {media_final}')
    

    