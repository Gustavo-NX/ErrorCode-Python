# Estilo/fonte: 0(nenhum) , 1(negrito) , 4(sublinhado) , 7(reverso/ao contrario)
# texto:        30(branco) , 31(vermelho) , 32(verde) , 33(amarelo) , 34 (azul), 35(roxo) , 36(ciano) , 37(cinza)
# cor.fundo:    40(branco) , 41(vermelho) , 42(verde) , 43(amarelo) , 44 (azul), 45(roxo) , 46(ciano) , 47(cinza)

# modelo base: \033[estilo;texto;fundo m

print('\033[1;33;44mOlá, mundo!\033[m')

num1 = 1
num2 = 2
print(f'Os valores são \033[1;32m{num1}\033[m e \033[1;35m{num2}\033[m !') #práticando