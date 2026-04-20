valor = int(input(' Digite um valor que deseja ver a tabuada: '))


print('')
print('TABUADA DO \033[1;33m{}\033[m'.format(valor))
print('-' * 12)
for i in range(11):
    print('\033[1;33m{}\033[m X \033[1;33m{:2}\033[m = \033[1;32m{}\033[m'.format(valor, i , valor*i))
print('-' * 12)