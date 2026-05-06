#Programa para aprovar o empréstimo bancário para a compra de uma casa, O programa vai perguntar o VALOR DA CASA, o SÁLARIO do comprador e 
#em QUANTOS ANOS ele vai pagar| Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado


valorCasa = float(input('Digite o valor da casa: '))
print('')
if valorCasa <= 0:
    print('\033[1;31mPor favor insira o valor correto da casa!\033[m\n')
else:
    salario = float(input('Digite seu salário: '))
    print('')
    if salario <= 0:
        print('\033[1;31mPor favor insira o valor correto do salário!\033[m\n')
    else:
        qtdAno = int(input('Digite em quantos anos planeja pagar: '))
        print('')
        if qtdAno <= 0:
            print('\033[1;31mPor favor insira corretamente a quantidade de anos planejada!\033[m\n')
        else:
            prestacaoMensal = valorCasa / (qtdAno * 12)
            if prestacaoMensal > (salario * 0.3):
                print('O valor mensal excedeu 30% do seu salário, por isso o banco não poderá conceder o empréstimo!')  
            else:
                print(f"""\033[1;35m
                {'='*30}
                        RECIBO BANCÁRIO
                {'='*30}
                Salário:         R$ {salario:>10.2f}
                Valor da casa:   R$ {valorCasa:>10.2f}
                Anos:            {qtdAno:>10}
                Prestação:       R$ {prestacaoMensal:>10.2f}
                {'='*30}
                \033[m""")