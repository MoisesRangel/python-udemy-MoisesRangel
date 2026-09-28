"""
iterável -> str, range, etc
iterador -> quem sabe entregar o valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu interador
For + Range
range -> range (start, stop, step)
"""

texto = iter('Luiz')
texto2 = 'Luiza'.__iter__()
print(texto)
print(texto2)

print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

texto3 = 'Rangel' # iterável
iterador = iter(texto3) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

for letra in texto3:
    print(letra)

#num = range(10,0,-1)
#for numero in num:
#    print(numero)