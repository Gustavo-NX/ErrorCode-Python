#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira ex( 6.127 = porção inteira 6)
from math import trunc

valor1 = float(input('Digite um número quebrado(com vírgula): '))

print('')
print(f'O número {valor1} tem como número inteiro {trunc(valor1)}')
