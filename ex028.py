#Programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi o escolhido pelo computador( escrever se perdeu ou venceu)
from random import randint
from playsound3 import playsound

cerebro = randint(0,5)
print('')
print('JOGO DA ADIVINHAÇÃO!')
print('')
valor = int(input('Digite o número entre 0 e 5 vamos ver se acertou o que eu estava pensando: '))


if valor == cerebro:
    print('PARABÉNS VOCÊ ACERTOU!')
    playsound("https://www.myinstants.com/media/sounds/app-12_1.mp3")
elif valor >= 6:
    print('digite um número válido!!')
    playsound("https://www.myinstants.com/media/sounds/voce-e-burro-burro-burro.mp3")
else:
    print('nao foi dessa vez')