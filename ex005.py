numero = int(input('Digite um valor: '))

print('Número escolhido: \033[1;36m{}\033[m'.format(numero))
print('Seu ANTECESSOR: \033[1;31m{}\033[m'.format(numero-1))
print('Seu SUCESSOR: \033[1;32m{}\033[m'.format(numero+1))
