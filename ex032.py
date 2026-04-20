#programa que leia o no e mostre se ele é bissexto
from datetime import date
ano = int(input('Digite 0 para checar ano atual ou algum ano aleatório: '))

print('')

if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')

print('')
