#Programa que faça o computador jogar Jokenpô.

import random
lista = ['Pedra','Papel','Tesoura']

escolha = str(input('Escolha entre Pedra , Papel ou Tesoura: ')).title()

random.shuffle(lista)


if escolha == 'Papel' and lista[0] == 'Pedra' or \
    escolha == 'Pedra' and lista[0] == 'Tesoura' or \
    escolha == 'Tesoura' and lista[0] == 'Papel':
    print(f'Resultado: {escolha} X {lista[0]}')
    print('VOCÊ GANHOU!')
elif escolha == lista[0]:
    escolha = str(input('Foi empate, tente novamente: ')).title()
    if escolha == 'Papel' and lista[0] == 'Pedra' or \
    escolha == 'Pedra' and lista[0] == 'Tesoura' or \
    escolha == 'Tesoura' and lista[0] == 'Papel':
        print(f'Resultado: {escolha} X {lista[0]}')
        print('VOCÊ GANHOU!')
    else: 
        print(f'Resultado: {escolha} X {lista[0]}')
        print('VOCÊ PERDEU!')
else:
    print(f'Resultado: {escolha} X {lista[0]}')
    print('VOCÊ PERDEU!')