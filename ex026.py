#leia frase (quantas letras "A", em que posição ela aparece a primeira vez, em qual a ultima vez) 

frase = input('Digite qualquer coisa: ').lower().split()
contador = frase.count('a')

print('')

print('-' * 10 + "RELATORORIO" + '-' * 10 )
print(f"""Na sua frase possui:
      Quantidade de A: {contador}
ata""")

#EM PRODUÇÃO