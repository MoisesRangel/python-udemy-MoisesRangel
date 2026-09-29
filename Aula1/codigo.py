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

pyautogui.click(x=420, y=375) # clica na caixinha de login
pyautogui.write('pyhtonimpressionador@gmail.com') # digita o email na caixinha de login
pyautogui.press('tab') # aperta tab para ir para a proxima caixa de senha
pyautogui.write('sua senha e muito dificilima ') # digita a senha da caixa de senha
pyautogui.press('tab') # aperta tab para ir para a proxima selecao
pyautogui.press('enter') # apertar enter para entrar no formulario

# Passo 3: Abrir base de dados
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)
for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=594, y=292)

    codigo = str(tabela.loc[linha,'codigo'])
    pyautogui.write(codigo)

    pyautogui.press('tab')
    marca = str(tabela.loc[linha,'marca'])
    pyautogui.write(marca)

    pyautogui.press('tab')
    tipo = str(tabela.loc[linha,'tipo'])
    pyautogui.write(tipo)

    pyautogui.press('tab')
    categoria = str(tabela.loc[linha,'categoria'])
    pyautogui.write(categoria)

    pyautogui.press('tab')
    precoUnitario = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(precoUnitario)

    pyautogui.press('tab')
    custo = str(tabela.loc[linha,'custo'])
    pyautogui.write(custo)

    pyautogui.press('tab')
    obs = str(tabela.loc[linha,'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    # voltar para o inicio da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos
