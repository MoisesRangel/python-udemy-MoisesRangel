"""
Exercicio
Peça ao usuário para digitar seu nome
Peça para o usuário para digitar sua idade
Se nome e idade forme digitados:
Exiba:
seu nome é {nome}
seu nome invertido é {nome invertido}
seu nome contem (ou não) espaços
seu nome tem {n} letras
A primeira letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
exiba "Desculpe, mas você deixou campos vazios. Encerrando..."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade:')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
    print(f'Sua idade é {idade}')
else:
    print(f'Desculpe, mas você deixou campos vazios. Encerrando...')