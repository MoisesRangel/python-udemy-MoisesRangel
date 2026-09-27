"""
Iterando strings com while
"""

# 0123456789
nome = 'Moises Rangel' # Iteraveis
tamanho_nome = len(nome)

contador = 0
nova_string = ''
while contador < tamanho_nome:
    nova_string += nome[contador]
    nova_string += '*'
    print(nova_string)
    contador += 1


print(nome)
print(tamanho_nome)

print('Fim do loop')