#O professor quer sortear ordem a ordem de apresentação leia os quatro alunos e mostre uma lista com a ordem.

import random ,time

aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

lista = [aluno1, aluno2, aluno3,aluno4]
random.shuffle(lista)
print('')
print('Carregando lista...')

time.sleep(1)

print('-'*50+'LISTA'+'-'*50)
print('')
print(f'Primeiro a apresentar é: {lista[0]} , Segundo: {lista[1]} , Terceiro: {lista[2]} , Quarto: {lista[3]}')