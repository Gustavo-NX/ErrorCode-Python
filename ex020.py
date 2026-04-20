#O professor quer sortear ordem a ordem de apresentação leia os quatro alunos e mostre uma lista com a ordem.

import random ,time

aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

lista = [aluno1, aluno2, aluno3,aluno4]
random.shuffle(lista)
print('')
print('\033[1;31mCarregando lista...\033[m')

time.sleep(1)

print('-'*50+'LISTA'+'-'*50)
print('')
print(f'Primeiro a apresentar é: \033[1;33m{lista[0]}\033[m , Segundo: \033[1;31m{lista[1]}\033[m , Terceiro: \033[1;31m{lista[2]}\033[m , Quarto: \033[1;31m{lista[3]}\033[m')