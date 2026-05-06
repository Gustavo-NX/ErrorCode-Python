#DESAFIO 41 - A confederação Nacional de natação precisa de um programador que leia o ano de nascimento de um atleta e moste sua categoria, de acordo com a idade,(até 9 = Mirim, até 14 = Infantil, até 19 = Junior, Até 20 = Senior, Acima = Master)

from datetime import date

anoAtual = date.today().year
nome = str(input('Escreva seu nome: '))
ano = int(input('\nDigite o ano que nasceu: '))

if ano <= 0 or ano > anoAtual:
    print('\n\033[1;31mDigite o ano correto!\033[m\n')
else:
    idade = anoAtual - ano
    if idade == 0:
        print('\n\033[1;36mNão é possivel matricular rescem-nascidos\033[m\n')
    elif idade <= 9:
        print(f"""\n
        {'_'*30}
                {nome}
        {'_'*30}
            Categoria: Mirim
        {'_'*30}""")         
    elif idade > 9 and idade <= 14:
        print(f"""\n
        {'_'*30}
                {nome}
        {'_'*30}
            Categoria: Infántil
        {'_'*30}""")
    elif idade > 14 and idade <= 19:
        print(f"""\n
        {'_'*30}
                {nome}
        {'_'*30}
            Categoria: Junior
        {'_'*30}""")
    elif idade > 19 and idade <= 20:
        print(f"""\n
        {'_'*30}
                {nome}
        {'_'*30}
            Categoria: Senior
        {'_'*30}""")
    else:
        print(f"""\n
        {'_'*30}
                {nome}
        {'_'*30}
            Categoria: Master
        {'_'*30}""")
