#Um professor quer sortear um dos seus quatro alunos para apagar o quadro . Faça um programa que ajude ele lendo o nome e escrevendo o escolhido

import random , time

aluno1 = input('Linha1: Escreva seu nome na lista: ')
aluno2 = input('Linha2: Escreva seu nome na lista: ')
aluno3 = input('Linha3: Escreva seu nome na lista: ')
aluno4 = input('Linha4: Escreva seu nome na lista: ')

lista = [aluno1, aluno2,aluno3,aluno4]

print('')
print('Escolhendo...')
time.sleep(1)
print('O aluno que vai apagar o quadro é {}'.format(random.choice(lista)))