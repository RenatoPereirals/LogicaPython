n = int(input("Quantas pessoas serao digitadas: "))

nome: [str] = [0 for x in range(0, n)]
idade: [int] = [0 for y in range(0, n)]
altura: [float] = [0 for z in range(0, n)]

for i in range(0, n):
    print(f"Dados da {i + 1}a pessoa: ")
    nome[i] = str(input("Nome: "))
    idade[i] = int(input("Idade: "))
    altura[i] = float(input("Altura: "))

soma = 0

for i in range(0, n):
    soma += altura[i]

media = soma / n

contMenos = 0

for i in range(0, n):
    if idade[i] < 16:
        contMenos += 1

pMenos = contMenos / n * 100

print(f"Altura media = {media:.2f}")
print(f"Pessoas com menos de 16 anos: {pMenos:.1f}%")
for i in range(0, n):
    if idade[i] < 16:
        print(nome[i])
