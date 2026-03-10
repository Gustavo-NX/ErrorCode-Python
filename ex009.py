valor = int(input(' Digite um valor que deseja ver a tabuada: '))


print('')
print('TABUADA DO {}'.format(valor))
print('--')
for i in range(11):
    print(f'{valor} X {i} = {valor*i}')
print('--')
