#Refaça o Desafio 35 dos triangulos, acrescentando o recurso de mostrar qual tipo de triangulo será formado,( Equilatero = todos os lados iguais, Isóceles: dois lados iguais, Escaleno = todos os lados diferentes)

lista = []
for i in range(3):
    numero = int(input(f'Digite o valor da {i+1}° reta: '))
    lista.append(numero)

if lista[0] + lista[1] > lista[2] and \
   lista[0] + lista[2] > lista[1] and \
   lista[1] + lista[2] > lista[0]:
    print('\033[1;32mAs três retas juntas formam um triângulo!!\033[m\n')
    if lista[0] == lista[1] and lista[0] == lista[2]:
        print('\033[1;33mE estre é um triângulo Equilatero!\033[m')
    elif lista[0] == lista[1] and lista[0] != lista[2] or \
         lista[1] == lista[2] and lista[1] != lista[0] or \
         lista[0] == lista[2] and lista[0] != lista[1]:
        print('\033[1;33mE estre é um triângulo Isóceles!\033[m')
    else:
        print('\033[1;33mE estre é um triângulo Escaleno!\033[m')
else:
    print('\033[1;31mNão é possível formar um triângulo!\033[m')