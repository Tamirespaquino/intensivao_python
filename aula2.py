# Lógica

import pandas as pd

# Passo 1: Importar a base de dados
tabela = pd.read_csv("telecom_users.csv") # o arquivo csv precisa estar no mesmo arquivo do código python
# se estiverem em pastas diferentes, precisa passar o caminho até o arquivo

# Passo 2: Visualizar a base de dados
display(tabela)

# Passo 3: Tratamento de dados (corrigir os problemas da base de dados)
# coluna inútil - informação que não ajuda, atrapalha
tabela = tabela.drop("Unnamed: 0", axis=1) #nome do que quer deletar e se é uma linha ou coluna
# axis=1 -> coluna; axis=0 -> linha. Vai adicionando o nome do que quer deletar
display(tabela)

# valores reconhecidos de forma errada
# object -> reconhece como texto
# int -> numero inteiro
# float -> numero com casa decimal
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # selecionando a coluna desejada e transformando ela em numerico
# coerce = palavra padrão para deixar vazio

print(tabela.info()) # mostra os tipos de cada linha e coluna 

# tratar valores vazios (NaN) - cada caso é um caso
tabela = tabela.dropna(how="all", axis=1) # excluir colunas vazias
# any - pelo menos algum valor vazio; all - todos completamente com valores vazios
tabela = tabela.dropna(how="any", axis=0)# excluir as linhas que tem algum valor vazio

print(tabela.info())

# Passo 4: Análise Inicial
print(tabela["Churn"].value_counts()) # conta os valores da tabela
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) # parametro de normalização que transforma em porcentagem

# Passo 5: Análise detalhada dos clientes
import plotly.express as px
# !pip install plotly

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x="Aposentado", color="Churn", color_discrete_sequence=["purple", "pink"])
    grafico.show()
