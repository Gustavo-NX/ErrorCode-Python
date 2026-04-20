#leia três números e diga qual o maior e qual o menor

lista = []
for i in range(3):
    numero = int(input(f'Digite o {i+1}° valor: '))
    lista.append(numero)

lista.sort()

print('')
print(f'O menor valor digitado é: {lista[0]}')
print(f'O meaior valor digitado é: {lista[2]}')
print('')
print(f'Ordem menor para o maior: {lista[0]} {lista[1]} {lista[2]}')
