dias = int(input('Quantos dias alugados do carro: '))
km = int(input('Quantos km andou: '))

calDia = dias * 60
calKm = km * 0.15

print('')
print('-' * 25,'RECIBO', '-'*25)
print('')
print(f'Dias: \033[1;35m{dias}\033[m + R$60 diaria')
print(f'Dias: \033[1;37m{km}\033[m + R$0.15 por Km')
print(f'Total a pagar = \033[1;32mR${calDia+calKm}\033[m')
