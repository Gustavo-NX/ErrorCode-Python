#Leia o nome de uma cidade e ele vai dizer se a cidade começa ou nao com o nome 'Santo'

cidade = input('Digite o nome de alguma cidade: ').strip()
santo = cidade.find('Santo')

if santo == 0:
    print('A cidade começa com Santo')
elif santo > 0:
    print('Está cidade não começa com o nome Santo')
else:
    print('Não consta o nome Santo nessa cidade')
