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
print('Altura: {:.2f}'.format(altura))
print('Largura: {:.2f}'.format(largura))
print('')
print('Para pintar uma parede com área de {}m²'.format(area))
print('Você vai precisar de {} Litros de tinta'.format(litros))
