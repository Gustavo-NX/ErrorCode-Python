#leia numero inteiro e mostre se é par ou impar

numero = int(input('Digite um núemro: '))
print('')

if numero % 2 == 0:
    print('\033[1;36mEste numero é par\033[m')
else:
    print('\033[1;34mEste número é impar\033[m')