#Leina nome e mostre primeiro e último nome Ex: Ana Maraia Souza primeiro= Ana , ultimo = Souza

nome = input('Qual seu nome: ').strip()
separado = nome.split()

print('')

print(f"""NOME: \033[1;33m{nome}\033[m
          
    Primeiro : \033[1;32m{separado[0]}\033[m

    Último   : \033[1;31m{separado[len(separado)-1]}\033[m""")