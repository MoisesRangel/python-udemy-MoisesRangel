"""Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamento
métodos úties:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10,20,30,40]
print(lista)

lista[2] = 300
del lista[2]
print(lista)
print(lista[2])
lista.append(50) # append() adiciona ao final
lista.pop() # pop() remove o ultimo item da lista
lista.append(90)
lista.append(80)
print(lista)