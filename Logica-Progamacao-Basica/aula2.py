# \r = carriage return, retorna o cursor para o inicio da linha, sobrescrevendo o que estava escrito.
# \n = new line, quebra de linha, pulando para a proxima linha.
# \r \n = CRLF; \n = LF
print(12, 34, sep='=') # o print recebe argumentos e separa por virgula.
print(56, 78, sep="=") # o print recebe argumentos como o sep de separador em que pode ser usado aspas simples ou duplas para poder separar os argumentos.
print(22, 33, sep="=", end="\n#") # o print recebe argumentos como o end de finalizador em que pode ser usado ao final da linha do print para pular para a proxima linha.
# Python é case sensitive, ou seja, diferencia maiúscula de minuscula.
# Print  <-- não existe