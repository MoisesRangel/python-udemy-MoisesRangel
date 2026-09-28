# dentro do for a variavel letra pode ser iniciada ali mesmo


texto = 'Python'
novoTexto = ''
for letra in texto:
    novoTexto += f'*{letra}'
    print(letra)
print(novoTexto + '*')