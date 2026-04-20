#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE: (todas as letras maiusculas, todas as letras minusculas, quantas letras ao todo sem considerar espaços, quantas tem o primeiro nmnome)

nome = input('Escreva seu nome: ')
dividido = nome.split()
print('')
print(f""" MOSTRANDO SEU NOME DE DIFERENTES MODOS
      
      MAIUSCULA: \033[1;32m{nome.upper()}\033[m
      
      minuscula: \033[1;31m{nome.lower()}\033[m
      
      qtd de letras: \033[1;33m{len(nome) - nome.count(' ')}\033[m
      
      qtd primeiro nome: \033[1;37m{len(dividido[0])}\033[m""")