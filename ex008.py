metro = int(input("Escreva um valor em metros: "))

centimetro = int(metro * 100)
milimetro = int(metro * 1000)

print('\n')

print("Aqui está a conversão")
print("")

print('centimetros: \033[1;34m{}\033[m'.format(centimetro))
print('')
print('milimetro: \033[1;35m{}\033[m'.format(milimetro))