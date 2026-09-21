# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira
# será avaliada naquele valor
# São consideradas false = 0, 0.0, False
# Também existe o tipo None que é usado para representar um não valor

print(True and False and True)
print (bool(' '))


entrada = input('[E]ntrar [S]air: ')
if entrada == 'E' or 'e':
    senha_digitada = input ('Senha: ')

senha_permitida = '123456'

if entrada == 'E' or 'e' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')