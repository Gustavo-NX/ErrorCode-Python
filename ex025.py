#leia nome de uma pessoa e diga se tem silva no nome

nome = input('Digite algum nome: ').strip()
silva = nome.find('Silva')
print('')

if silva == -1 :
    print('Não contem Silva neste nome')
else:
    print('Pelo nome completo vemos o sobrenome Silva')