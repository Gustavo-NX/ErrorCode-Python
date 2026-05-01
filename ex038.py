#Programa que leia dois números e compare o dizendo se o primeiro número é o maior, se o segundo é o maior, se não existe valor maior, os dois são iguais

num1 = int(input('Digite um número qualquer: '))
num2 = int(input('Agora outro número qualquer: '))
print('')

if num1 > num2:
    print(f'O primeiro número digitado: \033[1;32m{num1} é o maior!\033[m')
elif num2 > num1:
    print(f'O segundo número digitado: \033[1;36m{num2} é o maior!\033[m')
else:
    print('\033[1;31mOs dois números são iguais!\033[m')