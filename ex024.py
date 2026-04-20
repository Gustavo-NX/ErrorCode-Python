#Leia o nome de uma cidade e ele vai dizer se a cidade começa ou nao com o nome 'Santo'

cidade = input('Digite o nome de alguma cidade: ').strip()
santo = cidade.find('Santo')

if santo == 0:
    print('\033[1;32mA cidade começa com Santo\033[m')
elif santo > 0:
    print('\033[1;34mEstá cidade não começa com o nome Santo\033[m')
else:
    print('\033[1;31mNão consta o nome Santo nessa cidade\033[m')
