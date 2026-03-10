import time
salario = float(input('Digite seu salario: '))
porcentagemAumento = float(15 / 100)
aumento = salario + (salario * porcentagemAumento)
print('')

print('Você teve um aumento de R${}'.format(salario * porcentagemAumento))
print('')
print('Calculando salario atual...')
print('')
time.sleep(3)
print('Seu novo salario é de R${:.2f}'.format(aumento))