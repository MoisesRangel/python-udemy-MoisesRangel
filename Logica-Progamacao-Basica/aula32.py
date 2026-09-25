"""
Faça um programa que peça ao usuario para digitar um numero inteiro
informe se este numero é par ou impar. Caso um usuario nao digite um numero inteiro, informe que nao e um numero inteiro.

"""
numero_str = input('Digite um numero inteiro: ')

if numero_str.isdigit():
    numero = int(numero_str)
    if numero % 2 == 0:
        print(f'O numero {numero} é par')
    else:
        print(f'O numero {numero} não é par')
else:
    print('Você não digitou um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex.: Bom dia0-11, Boa  tarde 12-17 e Boa noite 18-23.
"""

hora = int(input('Digite a hora no formato 24h: '))

if hora >=0 and hora <= 11:
    print(f'Bom dia! São {hora}h')
elif hora >=12 and hora <=17:
    print(f'Boa tarde! São {hora}h')
elif hora >=18 and hora <=23:
    print(f'Boa noite! São {hora}h')
else:
    print('Digite uma hora válida. Encerrando...')

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto"; se tiver entre 5 e 6 letras escreva, "Seu nome é normal"; 
maior que 6 escreva " Seu nome é muito grande"
"""

nome = input('Digite o seu nome: ')
nome_tamanho = len(nome)
if nome_tamanho <=1:
    print(f'Seu nome tem pelo menos uma letra')
elif nome_tamanho >=2 and nome_tamanho <=4:
    print(f'O seu nome é curto')
elif nome_tamanho >=5 and nome_tamanho <=6:
    print(f'Seu nome é normal')
else:
    print(f'Seu nome é muito grande')