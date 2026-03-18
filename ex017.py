#Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triângulo retângulo calcule e mostre a hipotenusa
from math import sqrt, pow, trunc
import time

catOposto = int(input('Digite o valor do cateto oposto: '))
print('')
catAdjacente = int(input('Digite o valor do cateto adjacente: '))
print('')
print('Calculando....')
potencia = pow(catOposto,2) + pow(catAdjacente,2)
hipotenusa = sqrt(potencia)
time.sleep(1.5)
print('')

print(f'Cateto Oposto: {catOposto}')
print(f'Cateto Adjacente: {catAdjacente}')
print(f'Hipotenusa: {trunc(hipotenusa)}')