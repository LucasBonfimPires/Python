import Ações

papel = str(input("informe o código da ação que deseja consultar: "))


if papel == 'BBDC4' or papel == 'bbdc4':
    BBDC4 = Ações.bradesco(papel)
    print(BBDC4)
        
elif papel == 'ITUB3' or papel == 'itub3':
    ITUB3 = Ações.itau(papel)
    print(ITUB3)


