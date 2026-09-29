# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Abrir base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos


# Comandos mais usados:
#pyautogui.click -> clica
#pyautogui.write -> escreve um texto
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -: aperta um atalho

import pyautogui
import time
pyautogui.PAUSE = 2.5 # aguardar 2.5 segundo a cada comando
# Passo 1: Entrar no sistema da empresa
#   Abrir o navegador
pyautogui.press('win') # pressiona o botao windows do teclado
pyautogui.write('Chrome') # escreve chrome na aba de pesquisa
pyautogui.press('enter') # aperta enter no google chrome para abri a pagina

#   Acessar o link do sistema 

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' # adiciona o link do formulario a uma variavel
pyautogui.write(link) # escreve o link da aba de pesquisa do chrome
pyautogui.press('enter') # aperta o enter para acessar a pagina

#   Fazer uma pausa maior para o site carregar
time.sleep(3) # após acessar a página aguarda 3 segundos para a pagina carregar, pode variar o tempo dependendo do carregamento

# Passo 2: Fazer login
#   Clicar no campo de login
#   Digitar o login e senha

pyautogui.click(x=455, y=382) # clica na caixinha de login
pyautogui.write('pyhtonimpressionador@gmail.com') # digita o email na caixinha de login
pyautogui.press('tab') # aperta tab para ir para a proxima caixa de senha
pyautogui.write('sua senha e muito dificilima ') # digita a senha da caixa de senha
pyautogui.press('tab') # aperta tab para ir para a proxima selecao
pyautogui.press('enter') # apertar enter para entrar no formulario

# Passo 3: Abrir base de dados
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv('produtos.csv')
#print(tabela)
for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=511, y=256)
    pyautogui.write('MOLO000251')

    pyautogui.press('tab')
    pyautogui.write('Logitech')

    pyautogui.press('tab')
    pyautogui.write('Mouse')

    pyautogui.press('tab')
    pyautogui.write('categoria')

    pyautogui.press('tab')
    pyautogui.write('preco_unitario')

    pyautogui.press('tab')
    pyautogui.write('custo')

    pyautogui.press('tab')
    pyautogui.write('NaN')

    pyautogui.press('tab')
    pyautogui.press('enter')


# Passo 5: Repetir o passo 4 até acabar a lista de produtos
