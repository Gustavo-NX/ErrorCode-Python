#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE: (todas as letras maiusculas, todas as letras minusculas, quantas letras ao todo sem considerar espaços, quantas tem o primeiro nmnome)

nome = input('Escreva seu nome: ')
dividido = nome.split()
print('')
print(f""" MOSTRANDO SEU NOME DE DIFERENTES MODOS
      
      MAIUSCULA: {nome.upper()}
      
      minuscula: {nome.lower()}
      
      qtd de letras: {len(nome) - nome.count(' ')}
      
      qtd primeiro nome: {len(dividido[0])}""")