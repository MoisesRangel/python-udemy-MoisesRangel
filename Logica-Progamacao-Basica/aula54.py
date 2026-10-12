"""
Introdução ao desempacotamento
"""
# nomes = ['Maria', 'Joao', 'Flavio']
# nome1, nome2, nome3 = nomes
# ou
#nome1, nome2, nome3 = ['Maria', 'Joao', 'Flavio']
nome1, *resto = ['Maria', 'Joao', 'Flavio'] # mas resto fica feio, entao convencionalmente coloca *_ (underline)
nome1, *_ = ['Maria', 'Joao', 'Flavio']
print(nome1)
#print(nome2)
#print(nome3) 