# Operadores in e not in
# String são iteraveis
# Iteravel significa que você pode navegar item por item
# 0 1 2 3 4 5
# R a n g e l
# -6-5-4-3-2-1

nome = 'Rangel'
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print('a' in nome) # Retorna True
print('z' in nome) # Retorna False
print('y' not in nome) # Retorna True
print('2' not in nome) # Retorna True

name = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(encontrar, 'está em ', nome)
else:
    print(encontrar, 'não está em', nome)