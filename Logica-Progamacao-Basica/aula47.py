"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibildiade para o usuario digitar apenas uma letra.
- Qualquer letra que o usuario digitar, voce deve conferir se a letrar está na palavra secreta
- Se a letra digitada estiver na palavra secreta, exiba a letra
- Se a letra digitada não estiver na palavra secreta, exiba *
Faça a contagem de tentativas do seu usuário


"""

palavraSecreta = 'amor'
letrasAcertadas = ''
tentativas = 0

print(5*'*', 'Jogo da palavra secreta!', 5*'*')
print('Advinhe as letras corretas das palavras.')
print('Será sorteado algumas palavras e você terá algumas tentativas de acertar!')


while True:
    letraDigitada = input('Digite uma letra: ')

    tentativas += 1
    if len(letraDigitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letraDigitada in palavraSecreta:
        letrasAcertadas += letraDigitada

    palavraFormada = ''
    for letraSecreta in palavraSecreta:
        if letraSecreta in letrasAcertadas:
            palavraFormada += letraSecreta
        else:
            palavraFormada += '*'
    print(palavraFormada)

    if palavraFormada == palavraSecreta:
        print('Parabéns! Você acertou a palavra secreta!')
        print(f'Numero de tentativas foi {tentativas}')

        break
