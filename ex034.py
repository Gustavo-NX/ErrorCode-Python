# Programa que pergunte o salário de um funcionario e calcule o valor do seu aumento, para sálario superiores a 1.250 calcule aumento de 10% , e para inferioes ou iguais o aumento é de 15%

salario = float(input('Digite quanto você recebe de sálario: '))
print('')

if salario > 1250:
    aumento = (salario * 0.10)
    print(f'Você receberá um aumento de 10% equivalente a \033[1;33mR${aumento:.2f}\033[m, totalizando: \033[1;32mR${aumento + salario:.2f}\033[m')
else:
    aumento = salario * 0.15
    print(f'Você receberá um aumento de 15% equivalente a \033[1;33mR${aumento:.2f}\033[m, totalizando: \033[1;32mR${aumento + salario:.2f}\033[m')