import pyodbc

def conectar():
    dados_conexao = (
            "DRIVER={SQL Server}; SERVER=LUCAS-PC\SQLEXPRESS;  DATABASE=bovespa;" 
    )

    #criando conexão
    conexao = pyodbc.connect(dados_conexao)

    return conexao
