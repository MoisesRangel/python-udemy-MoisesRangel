# for in com listas
# Exiba os indices da lista

lista = ['Maria', 'Helena', 'Luiz'] # 0 1 2 | 3 itens

print(len(lista)) # Quantos itens essa lista tem
lista.append('Moises')

indices = range(len(lista)) # Essa lista vai de 0 até 3 itens, atribui a uma variavel

print(indices)

for indice in indices: # para cada indice dentro da lista com os indices
    print(indice, lista[indice]) # printa o indice