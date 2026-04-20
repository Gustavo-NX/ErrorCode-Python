#Leia a velocidade de um carro se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que tomou multa e calcule quando vai custar a multa, sabendo que vale 7 reais por cada Km acima do limite 

velocidade = int(input('Digite a velocidade do carro: '))

multa = (velocidade - 80) * 7

if velocidade > 80 and velocidade < 100:
    print('')
    print('Você tomou uma multa!')
    print(f'Valor da multa: \033[1;36mR$ {float(multa):.2f}\033[m')
elif velocidade >= 100:
    print('')
    print('Você tomou uma multa bem grave!')
    print(f'Valor da multa: \033[1;31mR$ {float(multa):.2f}\033[m')