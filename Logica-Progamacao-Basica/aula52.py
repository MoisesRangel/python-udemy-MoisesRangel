""" cuidado com dados mutaveis
= - copiar o valor (imutaveis)
= - apontar para o mesmo valor na memoria (mutavel)
"""

#nome = 'luiz'
#noutraVariavel = nome
#nome = 'Joao'
#print(nome)
#print(noutraVariavel)


listaA = ['Luiz', 'Maria']
listaB = listaA.copy()

listaA.append('Joao')
listaA[0] = 'Qualquer coisa'
print(listaA)
print(listaB)