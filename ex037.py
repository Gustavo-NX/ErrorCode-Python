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
        valor1 = numero / 2

#EM ANDAMENTO