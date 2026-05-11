#DESAFIO 37 - Programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão ( Binário , Octal, Hexadecimal)

numero = int(input('Digite uma número inteiro qualquer: '))
if numero <= 0:
    print('\033[mDigite um valor válido\033[m')
else:
    print('')
    print(f""" 
    {'-'*30}
            Esolha Entre
    {'-'*30}
        1- Binário
        
        2- Octal
        
        3- Hexadecimal
    {'-'*30}\n""")
    escolha = int(input('Digite Aqui: '))
    if escolha == 1:
        print(f'{numero} convertido para binário: {bin(numero)[2:]}\n')
    elif escolha == 2:
        print(f'{numero} convertido para binário: {oct(numero)[2:]}\n')
    else:
        print(f'{numero} convertido para binário: {hex(numero)[2:]}\n')

#EM ANDAMENTO