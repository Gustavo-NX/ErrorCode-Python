#Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triângulo retângulo calcule e mostre a hipotenusa
from math import hipot
import time

catOposto = float(input('Digite o valor do cateto oposto: '))
print('')
catAdjacente = float(input('Digite o valor do cateto adjacente: '))
print('')
print('Calculando....')
# potencia = pow(catOposto,2) + pow(catAdjacente,2)
# hipotenusa = sqrt(potencia)
hipotenusa = hipot(catOposto, catAdjacente)
time.sleep(1.5)
print('')

print(f'Cateto Oposto: \033[1;35m{catOposto:.2f}\033[m')
print(f'Cateto Adjacente: \033[1;37m{catAdjacente:.2f}\033[m')
print(f'Hipotenusa: \033[1;31m{hipotenusa:.2f}\033[m')