import time

largura = float(input('Me passe a largura da parede que deseja pintar: '))
altura  = float(input('Me passe a altura da parede que deseja pintar: '))
area = largura * altura

#com 1(um litro) é possivel pintar 2m²(dois metros quadrados))
litros = area / 2


print('Calculando...')
time.sleep(1.5)

print('')
print('')
print('INFORMAÇÕES')
print('Cada litro pinta 2m²')
print('')
print('Sua parede tem:')
print('Altura: \033[1;35m{:.2f}\033[m'.format(altura))
print('Largura: \033[1;35m{:.2f}\033[m'.format(largura))
print('')
print('Para pintar uma parede com área de \033[1;34m{}\033[mm²'.format(area))
print('Você vai precisar de \033[1;36m{}\033[m Litros de tinta'.format(litros))
