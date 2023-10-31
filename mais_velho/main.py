n = int(input("Quantas pessoas voce vai digitar: "))

nome: [str] = [0 for x in range(0, n)]
idade: [int] = [0 for y in range(0, n)]

for i in range(0, n):
    print(f"Dados da {i + 1}a pessoa:")
    nome[i] = str(input("Nome: "))
    idade[i] = int(input("Idade: "))

maisVelho = idade[0]
nomeVelho = nome[0]

for i in range(0, n):
    if idade[i] > maisVelho:
        maisVelho = idade[i]
        nomeVelho = nome[i]

print(f"PESSOA MAIS VELHA: {nomeVelho}")
