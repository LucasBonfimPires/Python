from bs4 import BeautifulSoup
from datetime import timedelta, date
import requests
import ConectarSQL


#banco de dados

conexao = ConectarSQL.conectar()

def bradesco(papel):
    URL = 'https://br.investing.com/equities/bradesco-pn-n1'
    BBDC4 = requests.get(URL)
    #organiza o html com soup
    soup = BeautifulSoup(BBDC4.text, 'html.parser')
    #busca o valor da ação no dia anterior e armazena na variavel "cotacao" tipo Float
    cotacao = soup.find(class_='key-info_dd-numeric__2cYjc').get_text()
    cotacao = cotacao.replace(',', '.')
    cotacao = float(cotacao)
    #data da cotação (sempre 1 dia antes)
    dia = date.today() - timedelta(days = 1)
    
    
    cursor = conexao.cursor()
    
    comando = f"""INSERT  INTO bradesco
                (papel, cotacao, diaAno)
                VALUES
                ('{papel}', '{cotacao}', '{dia}')
                """
    cursor.execute(comando)
    cursor.commit()
    
    
    return f'Cotação: {cotacao}, dia: {dia}'

def itau(papel):
    URL = 'https://br.investing.com/equities/itauunibanco-on-edj-n1'
    ITUB3 = requests.get(URL)
    #organiza o html com soup
    soup = BeautifulSoup(ITUB3.text, 'html.parser')
    #busca o valor da ação no dia anterior e armazena na variavel "cotacao" tipo Float
    cotacao = soup.find(class_='key-info_dd-numeric__2cYjc').get_text()
    cotacao = cotacao.replace(',', '.')
    cotacao = float(cotacao)
    #data da cotação (sempre 1 dia antes)
    dia = date.today() - timedelta(days = 1)
    
    
    cursor = conexao.cursor()
    
    comando = f"""INSERT  INTO itau
                (papel, cotacao, diaAno)
                VALUES
                ('{papel}', '{cotacao}', '{dia}')
                """
    cursor.execute(comando)
    cursor.commit()
    
    
    return f'Cotação: {cotacao}, dia: {dia}'