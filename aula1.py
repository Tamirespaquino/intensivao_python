# pip install pyautogui
# pip install pyperclip

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1 # precisa desse tempo entre um comando e outro para conseguir rodar

# Passo 1: Entrar no sistema (link do drive)

# para abrir o navegador considerando que esteja fechado
pyautogui.press("win") # ele clica no ícone do windows para abrir a barra de busca do SO
pyautogui.write("chrome") # digita o nome do navegador que deseja
pyautogui.press("enter") # abre navegador

pyautogui.hotkey("ctrl", "t") # abrinco uma aba
pyperclip.copy("https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh") # copiando o link
pyautogui.hotkey("ctrl", "v") # colando o link
pyautogui.press("enter") # entrando no sistema

# carregar o sistema (demorar 5 s apenas nesta etapa)
time.sleep(5)

# Passo 2: Navegar no sistema (até a pasta Exportar)

pyautogui.click(x=974, y=676, clicks=2) # clicks indica a quantidade de click que ele dá dentro da pasta
# para saber a posição correta do mouse é só rodar o pyautogui.position(), mas isso depende da resolução da tela do PC
# ou seja, isso muda de PC para PC. Se quiser que seja de forma automatica em qualquer PC, precisa usar outra ferramenta (terceira aula)

# Passo 3: Fazer download da base de vendas

pyautogui.click(x=922, y=828) # clicar no arquivo
pyautogui.click(x=3339, y=404) # clicar nos 3 pontos
pyautogui.click(x=2890, y=1406) # clicar em fazer download

time.sleep(5) # esperar o download

# Passo 4: Importar a base de dados de vendas para o Python
# se não estiver usando jupyter notebook, instalar: pandas, numpy, openpyxl
import pandas as pd

tabela = pandas.read_excel(r"C:\Users\Python\Download\Vendas - Dez.xlsx") 
# r é um caracter especial que diz para o python não ler as barras do caminho como caracter especial
# nomear com uma variavel fica mais fácil para entender
# também é importante descrever o caminho daonde vc gostaria que o arquivo seja baixado
display(tabela)

# Passo 5: Calcular o faturamento e quantidade de produtos vendidos (os indicadores)

faturamento = tabela["Valor Final"].sum()
# para selecionar coluna na tabela é só fazer tabela["Valor Final"]
qtde_produtos = tabela["Quantidade"].sum()
display(faturamento)
display(qtde_produtos)

# Passo 6: Enviar e-mail para diretoria

# Abrir e-mail
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

# Clicar no botão de escrever
pyautogui.click(x=282, y=463)

# Preencher o destino
pyautogui.write("emailparateste@gmail.com")
pyautogui.press("tab") # seleciona o e-mail
pyautogui.press("tab") # muda para o campo de assunto

# Preencher o assunto
pyperclip.copy("Relatório de Vendas") # para todo texto com caracter especial
pyautogui.hotkey("ctrl", "v") # precisa fazer o processo de copiar e colar o texto
pyautogui.press("tab") # mudar para o corpo do e-mail

# Escrever o e-mail
texto = f"""
Prezados, bom dia!

Encaminho os resultados de vendas deste mês. 
O faturamento foi de R$ {faturamento:,.2f}. # depois do : é a formatação do numero
A quantidade de produtos foi de {qtde_produtos:,}. 

Atenciosamente,

Pessoa Aleatória.
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# Clicar em enviar
pyautogui.hotkey("ctrl", "v")
