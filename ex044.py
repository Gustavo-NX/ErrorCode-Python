#Calcule o valor a ser pago por um produto considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO ( a vista/cheque = 10% desconto, a vista cartão = 5%desconto, em até 2x = preço normal, 3x ou mais = 20% de juros)

valorProduto = float(input('\nDigite o valor do produto: '))
print('')

print(f"""
    {'-'*25}
        FORMA DE PAGAMENTO 
    {'-'*25}
    
    1- A vista / Cheque
    2- A vista no cartão
    3- Parcelado
    {'-'*25}""")
escolha = int(input('Digite uma das opções: '))
print('')

if escolha == 1:
    print(f"""
    {'-'*25}
            COMPROVANTE
    {'-'*25}
    
    Valor do protudo: {valorProduto}
    10% de desconto a vista
    
    TOTAL: {valorProduto - (valorProduto * 0.1)}\n""")

#Em Andamento