#Leina nome e mostre primeiro e último nome Ex: Ana Maraia Souza primeiro= Ana , ultimo = Souza

nome = input('Qual seu nome: ').strip()
separado = nome.split()

print('')

print(f"""NOME: {nome}
          
    Primeiro : {separado[0]}

    Último   : {separado[len(separado)-1]}""")