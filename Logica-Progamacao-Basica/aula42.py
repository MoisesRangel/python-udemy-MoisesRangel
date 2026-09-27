frase = 'O python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum.'

i = 0
qtd = 0
maiorLetra = ''
while i < len(frase):
    letraAtual = frase[i]
    qtdAtual = frase.count(letraAtual)

    if letraAtual == ' ':
        i += 1
        continue

    if qtd < qtdAtual:
        qtd = qtdAtual
        maiorLetra = letraAtual

    i += 1


print(f'A letra que apareceu mais vezes foi {maiorLetra} que apareceu {qtd}x')