#Um programa que pergunte a distância de uma viagem em KM. Calcule preço da passagem, cobrando 0,50 por km para viagens de até 200km e 0,45 para viagens mais longas

distancia = float(input('Digite a distância da sua viagemem quilometragem(KM): '))

if distancia <= 200:
    passagem = (distancia * 0.50)
    print(f"""\033[1;30m
          ||||||||||||||||||||||||||||
                Custo da viagem
          
          Distancia: \033[1;31m{distancia}\033[m
          Cobrança  por km: R$ 0,50

          Valor da passagem: \033[1;36mR${passagem:.2f}\033[m
          ||||||||||||||||||||||||||||\033[m""")
else:
    passagem = (distancia * 0.45)
    print(f"""
        ||||||||||||||||||||||||||||||||||||||
                Custo da viagem
          
          Distancia: {distancia}
          Cobrança  por km: R$ 0,45

            Valor da passagem: R${passagem:.2f}
        ||||||||||||||||||||||||||||||||||||||""")