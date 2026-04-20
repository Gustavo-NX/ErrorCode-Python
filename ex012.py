produto = float(input('Insira o valor do produto: '))
desconto = 50 * 0.05
print('')

print("Carrinho: ")
print("Produto vale: \033[1;36m{}\033[m".format(produto))
print("Desconto \033[1;32m5%\033[m")
print('')
print('Valor a pagar: \033[1;31mR${}\033[m'.format(produto - desconto))