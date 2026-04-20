#leia três números e diga qual o maior e qual o menor

lista = []
for i in range(3):
    numero = int(input(f'Digite o {i+1}° valor: '))
    lista.append(numero)

lista.sort()

print('')
print(f'O menor valor digitado é: \033[1;31m{lista[0]}\033[m')
print(f'O maior valor digitado é: \033[1;32m{lista[2]}\033[m')
print('')
print(f'Ordem menor para o maior: \033[1;33m{lista[0]} {lista[1]} {lista[2]}\033[m')
