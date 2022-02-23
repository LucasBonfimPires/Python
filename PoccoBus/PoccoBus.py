import pandas as pd


#Inicialmente é Verificado se o arquivo "poccoBus" existe no diretório em que o python esta localizado
#caso o script não localize o arquivo "PoccoBus" é gerado uma lista com todos assento  do onibus e depois convertido
#em um dataframe pandas. No fim do código todas alterações são salvas e é gerado um arquivo salvando as informações.
#Quando o código é executado novamente, ele faz a consulta diretamente no arquivo .txt

#temos um menu com 3 opções onde é possível realizar reservas, cancelamentos ou apenas consultar as poltronas
#disponiveis.
try:
    assento  = pd.read_csv('PoccoBus')
except FileNotFoundError:
    print('Não foi possível abrir a lista')
    assento  = {'reserva':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 , 20, 21, 22, 23, 24, 25, 26, 27, 28]}
    assento  = pd.DataFrame(assento)

#função para reserva de assentos
def reservar():
    continuar = 1
    while continuar == 1:
        #Recebe o número da poltrona a reservar, caso digite um valor diferente de INT solicita correção
        print(assento)
        try:
            poltrona = int(input('Poltrona: '))
        except ValueError:
            print(assento)
            poltrona = int(input('Valor INVÁLIDO, tente novamente: '))
        
        
            
        #Verifica se a poltrona é valida, se for maior que 28 ou valor negativo entra em looping
        if poltrona > 28 or poltrona < 0:
            while poltrona > 28 or poltrona < 0:
                poltrona = int(input('Poltrona inválida Poltrona\nInforme uma poltrona válida: '))
                
        #Verifica disponibilidade da poltrona 1
        if poltrona == 0:
            print('Esse é o banco de motorista, poltrona para passageiros apartir da poltrona 1')
            
        
        #verifica disponibilidade das poltronas 1 ao 28 
        if poltrona >= 1:
            if (assento.loc[poltrona - 1] == f'{poltrona} - reservado').bool():
                print(f'A poltrona {poltrona} ja foi vendida')
            else:
                print(f'{poltrona} livre!')
                if poltrona == poltrona:
                    assento.loc[poltrona - 1] = assento.loc[poltrona - 1].replace({f'{poltrona}': f'{poltrona} - reservado'})
        
            
        #verifica se o usuário deseja continuar, se não sai do loop
        continuar = int(input('Nova reserva? 1 - sim / 2 - não --: ' ))
        if continuar <= 0 or continuar > 2:
            continuar = int(input('Opção inválida\nReservar mais 1 poltrona? 1 - sim / 2 - não --: ' ))


#função para cancelamento de reservas
def cancelar():
    continuar = 1
    while continuar == 1:    
    #Recebe o número da poltrona a reservar, caso digite um valor diferente de INT solicita correção
        print(assento)
        try:
            poltrona = int(input('Poltrona a ser cancelada: '))
        except ValueError:
            print(assento)
            poltrona = int(input('Valor INVÁLIDO, tente novamente: '))
        
        
            
        #Verifica se a poltrona é valida, se for maior que 28 ou valor negativo entra em looping
        if poltrona > 28 or poltrona < 0:
            while poltrona > 28 or poltrona < 0:
                poltrona = int(input('Poltrona inválida Poltrona\nInforme uma poltrona válida: '))
                
        #Verifica disponibilidade da poltrona 1
        if poltrona == 0:
            print('Esse é o banco de motorista, poltrona para passageiros apartir da poltrona 1')
            
        
        #verifica disponibilidade das poltronas 1 ao 28 
        if poltrona >= 1:
            if (assento.loc[poltrona - 1] == f'{poltrona} - reservado').bool():
                assento.loc[poltrona - 1] = assento.loc[poltrona - 1].replace({f'{poltrona} - reservado': f'{poltrona}'})
            else:
                print(f'A poltrona: {poltrona} não está reservada. ')
                
    
        #verifica se deseja continuar o cancelamento de outras reservas
        continuar = int(input('Cancelar outra reserva? 1 - sim / 2 - não --: ' ))
        if continuar <= 0 or continuar > 2:
            continuar = int(input('Opção inválida\nCancelar outra reserva? 1 - sim / 2 - não --: ' ))


#função de confirmação de compra
def confirmar():
    compra = int(input('Confirmar Alterações? 1 - Sim / 2 - Não'))
    if compra == 1:
        assento.to_csv('PoccoBus', index = False)
        print(assento)
        print('\n\nSALVO')
    else:
        print('Alterações canceladas')
        
        
#executa o sistema de vendas
print("="*20)
print('Bem-vindo ao PoccoBus')
print("="*20)
print('Escolha uma das opções:\n[1] - Compra de reservas\n[2] - Cancelamento de reservas\n[3] - Visualizar poltronas')
menu = int(input('Deseja Cancelar ou Reservar?'));

#executa a função de reservas e por fim faz uma verificação para salvar as alterações
if menu == 1:
    reservar()
    confirmar()
#executa a função de cancelar e por fim faz uma verificação para salvar as alterações
elif menu == 2:
    cancelar()
    confirmar()
#exibe todas as poltronas do onibus    
elif menu == 3:
    print(assento)

