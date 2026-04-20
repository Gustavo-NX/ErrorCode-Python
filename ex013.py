import time
salario = float(input('Digite seu salario: '))
porcentagemAumento = float(15 / 100)
aumento = salario + (salario * porcentagemAumento)
print('')

print('Você teve um aumento de \033[1;32mR${:.2f}\033[m'.format(salario * porcentagemAumento))
print('')
print('Calculando salario atual...')
print('')
time.sleep(3)
print('Seu novo salario é de \033[1;32mR${:.2f}\033[m'.format(aumento))