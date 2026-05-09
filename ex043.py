#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: (abaixo de 18.5 = abaixo do peso, entre 18.5 e 25 = peso ideal, 25 até 30 = Sobrepeso, 30 até 40 = Obesidade, Acima de 40 = Obesidade mórbida). 

altura = float(input('\nEscreva sua altura: '))
print('')
peso = float(input('Agora seu peso: '))
print('')

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"""
    {'_'*25}
    |        TABELA         |
    {'_'*25}
    | altura: {altura}           |
    {'_'*25}
    | Peso: {peso}            |
    {'_'*25}
    | Status: abaixo do peso|
    {'-'*25}\n""")
elif imc >= 18.5 and imc < 25:
    print(f"""
    {'_'*25}
    |        TABELA         |
    {'_'*25}
    | altura: {altura}           |
    {'_'*25}
    | Peso: {peso}            |
    {'_'*25}
    | Status: com ideal     |
    {'-'*25}\n""")
elif imc >= 25 and imc < 30:
    print(f"""
    {'_'*25}
    |        TABELA         |
    {'_'*25}
    | altura: {altura}           |
    {'_'*25}
    | Peso: {peso}            |
    {'_'*25}
    | Status: com sobrepeso |
    {'-'*25}\n""")
elif imc >= 30 and imc < 40:
    print(f"""
    {'_'*25}
    |        TABELA         |
    {'_'*25}
    | altura: {altura}           |
    {'_'*25}
    | Peso: {peso}            |
    {'_'*25}
    | Status: Obeso         |
    {'-'*25}\n""")
else:
    print(f"""
    {'_'*30}
    |       TABELA               |
    {'-'*30}
    | Altura: {altura}                |
    {'_'*30}
    | Peso: {peso}                |
    {'_'*30}
    | Status: Obesidade mórbida  |
    {'-'*30}\n""")