#DESAFIO 39 - Programa que leia ano de nascimento e informe de acordo com usa idade,( Se ele ainda vai se alistar ao serviço militar, se é hora de se alistar, se passou o tempo) deve mostrar quanto tempo falta ou quanto já passou
from datetime import date

ano = date.today().year
anoNascimento = int(input('Digite o ano que nasceu: '))
print('')
if anoNascimento <= 0 or anoNascimento > ano:
    print('\033[1;31mDigite o ano correto!\033[m\n')
else:
    idade = ano - anoNascimento
    if idade == 0:
        print('\033[1;36mO recêm nascido se alistará quando efetuar 18 anos\033[m\n')
    elif idade == 18:
        print('\033[1;32mVocê deve se alistar este ano, boa sorte!\033[m\n')
    elif idade < 18:
        faltaIdade = 18 - idade
        print(f'\033[1;33mVocê deverá se alistar em {faltaIdade} anos!\033[m\n')
    else:
        passouIdade = idade - 18
        print(f'\033[1;34mJá faz {passouIdade} anos que você passou pelo alistamento!\033[m\n')