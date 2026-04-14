#leia três números e diga qual o maior e qual o menor
from random import randint

lista = []
for i in range(3):
    numero = int(input(f'Digite o {i+1}° valor: '))
    lista.append(numero)


if lista[0] > lista[1]:
    lista[0], lista[1] = lista[1], lista[0]
    if lista[1] > lista[2]:
        lista[2], lista[1] = lista[1], lista[2]
        if lista[0] > lista[1]:
            lista[0], lista[1] = lista[1], lista[0]
elif lista[0] < lista[1] > lista[2]:
    lista[2], lista[1] = lista[1], lista[2]
    if lista[0] > lista[1]:
        lista[0], lista[1] = lista[1], lista[0]

print('')
print(f'Ordem menor para o maior: {lista[0]} {lista[1]} {lista[2]}')
