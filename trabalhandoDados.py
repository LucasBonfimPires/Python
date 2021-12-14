import pandas as pd
import ConectarSQL
#aqui você pode trabalhar com manipulação dos dados dentro do SQL

conexao = ConectarSQL.conectar()

sql = "SELECT papel, cotacao FROM bradesco"
#lê o comando sql dentro do pandas
df = pd.read_sql(sql, conexao)



print(df)