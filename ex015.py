dias = int(input('Quantos dias alugados do carro: '))
km = int(input('Quantos km andou: '))

calDia = dias * 60
calKm = km * 0.15

print('')
print('-' * 25,'RECIBO', '-'*25)
print('')
print(f'Dias: {dias} + R$60 diaria')
print(f'Dias: {km} + R$0.15 por Km')
print(f'Total a pagar = R${calDia+calKm}')
