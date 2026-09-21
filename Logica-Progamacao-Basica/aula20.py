primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if (primeiro_valor > segundo_valor):
    print('O', primeiro_valor, 'é maior que o', segundo_valor)
elif (segundo_valor > primeiro_valor):
    print('O', segundo_valor, 'é maior que o', primeiro_valor)
else:
    print('Valores digitados incorretos, encerrando o programa....')