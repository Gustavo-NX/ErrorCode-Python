#leia frase (quantas letras "A", em que posição ela aparece a primeira vez, em qual a ultima vez) 

frase = input('Digite qualquer coisa: ').lower().strip()

print('')

print('-' * 10 + "RELATORORIO" + '-' * 10 )
print(f"""Na sua frase possui:
      Quantidade de letras A: {frase.count('a')}
      A primeira letra A aparece na {frase.find('a') + 1}° posição 
      A última letra A aparece na {frase.rfind('a') + 1 - frase.count(' ')}° posição 
""")

#EM PRODUÇÃO