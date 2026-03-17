valor = int(input(' Digite um valor que deseja ver a tabuada: '))


print('')
print('TABUADA DO {}'.format(valor))
print('-' * 12)
for i in range(11):
    print('{} X {:2} = {}'.format(valor, i , valor*i))
print('-' * 12)