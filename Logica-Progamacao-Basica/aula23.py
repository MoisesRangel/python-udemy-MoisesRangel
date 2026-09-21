# operador lógico not
# usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if senha != '123456':
    print('Senha incorreta...')

if not senha:
    print('Senha incorreta...')

print(not True) # False
print(not False) # True