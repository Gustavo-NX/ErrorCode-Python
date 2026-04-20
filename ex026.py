#leia frase (quantas letras "A", em que posição ela aparece a primeira vez, em qual a ultima vez) 

frase = input('Digite qualquer coisa: ').lower().strip()

print('')

print('-' * 10 + "RELATORORIO" + '-' * 10 )
print(f"""Na sua frase possui:
      Quantidade de letras A: \033[1;36m{frase.count('a')}\033[m
      A primeira letra A aparece na \033[1;32m{frase.find('a') + 1}°\033[m posição 
      A última letra A aparece na \033[1;33m{frase.rfind('a') + 1 - frase.count(' ')}°\033[m posição 
""")