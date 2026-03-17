celsius = float(input('Está quantos graus lá fora ? '))
kelvin = celsius + 273.15
fahrenheit = (celsius * 1.8)+32

print('*' * 50)
print('De {:.2f} graus Celsius(°C)'.format(celsius))
print('Veja a conversão em:')
print('Fahrenheit(°F): {:.2f}'.format(fahrenheit))
print('Kelvin(°K): {:.2f}'.format(kelvin))
print('*' * 50)


# Celsius para Kelvin: K = C + 273.15

# Kelvin para Celsius: C = K - 273.15

# Celsius para Fahrenheit: F = (C * 1.8) + 32

# Fahrenheit para Celsius: C = (F - 32) / 1.8

# Fahrenheit para Kelvin: K = (F - 32) / 1.8 + 273.15