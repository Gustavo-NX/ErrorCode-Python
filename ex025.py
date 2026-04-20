#leia nome de uma pessoa e diga se tem silva no nome

nome = input('Digite algum nome: ').strip()
silva = nome.find('Silva')
print('')

if silva == -1 :
    print('\033[1;31mNão contem Silva neste nome\033[m')
else:
    print('\033[1;32mPelo nome completo vemos o sobrenome Silva\033[m')