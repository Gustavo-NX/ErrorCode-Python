#Um programa que leia o comprimento de três retas e diga ao usuârio se ele pode ou não formar um triângulo

lista = []
for i in range(3):
    numero = int(input(f'Digite o valor da {i+1}° reta: '))
    lista.append(numero)

if lista[0] + lista[1] > lista[2] and \
   lista[0] + lista[2] > lista[1] and \
   lista[1] + lista[2] > lista[0]:
    print('\033[1;32mAs três retas juntas formam um triângulo!!\033[m')
else:
    print('\033[1;31mNão é possível formar um triângulo!\033[m')