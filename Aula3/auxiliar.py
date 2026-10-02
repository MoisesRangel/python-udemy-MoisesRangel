# listas

nome = ['lira', 'gui', 'thalia', 'mae']

# pegar uma informação de uma lista

fulano = nome[0]
print(fulano)

#adicionar informações
nome.append("Rafael")

#dicionarios
pessoa = {'nome': 'Lira', 'idade':'32', 'peso':'68', 'cidade':'Rio de Janeiro'}
peso = pessoa['peso']

# como vamos usar 

listaMensagens = []

mensagem1 = {'role': 'user', 'content':'fala galera'} # role = cargo; content = conteudo
mensagem2 = {'role': 'assistant', 'content':'resposta da ia'}# role = cargo; content = conteudo

listaMensagens.append(mensagem1)
listaMensagens.append(mensagem2)

print(listaMensagens)