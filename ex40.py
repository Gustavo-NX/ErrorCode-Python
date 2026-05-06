#DESAFIO 40 - Leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final de acordo com a média (abaixo de 5.0 = reprovado , entre 5,0 e 6,9 = recuperação, 7.0 ou superior = aprovado)

nota1 = float(input('\nDigite sua primeira nota: '))
print('')
nota2 = float(input('Digite sua segunda nota: '))
print('')
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'\033[1;31mMÉDIA FINAL: {media:.1f} , você REPROVOU!\033[m\n')
elif media >= 5.0 and media < 7.0:
    print(f'\033[1;33mMÉDIA FINAL: {media:.1f} , você está de RECUPERAÇÃO!\033[m\n')
else:
    print(f'\033[1;32mMÉDIA FINAL: {media:.1f} , parabéns você foi APROVADO!\033[m\n')