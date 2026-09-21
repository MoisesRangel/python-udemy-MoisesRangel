"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - _ ou -
Ex.: 0>-100, 1.f
Conversion flags - !r !s !a __repr__ ___str___
"""
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.5497987984:0=+10,.1f}')
print(f'{variavel!r}')