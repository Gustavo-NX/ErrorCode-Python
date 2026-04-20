saldocarteira = float(input('Digite quanto tem na carteira: R$'))
conversao = saldocarteira / 5.16
print('')
print('Você pode comprar \033[1;32m${:.2f}\033[m dolares'.format(conversao))