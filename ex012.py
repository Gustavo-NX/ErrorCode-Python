produto = float(input('Insira o valor do produto: '))
desconto = 50 * 0.05
print('')

print("Carrinho: ")
print("Produto vale: {}".format(produto))
print("Desconto 5%")
print('')
print('Valor a pagar: R${}'.format(produto - desconto))