m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

mat: [[float]] = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    print(f"Digite os elementos da {i+1}a linha: ")
    for j in range(0, n):
        mat[i][j] = int(input())

vet: [float] = [0 for x in range(m)]

for i in range(0, m):
    soma = 0
    for j in range(0, n):
        soma += mat[i][j]
    vet[i] = soma

print("VETOR GERADO:")
for i in range(0, m):
    print(f"{vet[i]:.1f}")
