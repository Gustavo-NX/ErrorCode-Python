#programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. ex: 1834 (unidade 4 , dezena 3 ,centea: 8, milhar: 1)

numero = int(input('Escreva um número entre 0 a 9999: '))
m = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
u = numero // 1 % 10 # a vaviavel u não precisa da conta (numero // 1 % 10) porem foi mantido para ficar mais organizado


print('')
print(f"""  DADOS  
      Número escolhido: {numero}
      
      Milhar: {m}
      Centena: {c}
      Dezena: {d}
      Unidade: {u}""")