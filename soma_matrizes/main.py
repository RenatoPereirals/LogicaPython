m = int(input("Quantas linhas vai tera cada matriz? "))
n = int(input("Quantas colunas vai tera cada matriz? "))

A: [[int]] = [[0 for x in range(n)] for x in range(m)]
B: [[int]] = [[0 for x in range(n)] for x in range(m)]

print("Digite os elementos da matriz A:")
for i in range(0, m):
    for j in range(0, n):
        A[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Digite os elementos da matriz B:")
for i in range(0, m):
    for j in range(0, n):
        B[i][j] = int(input(f"Elemento [{i},{j}]: "))

soma: [[int]] = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    for j in range(0, n):
        soma[i][j] = A[i][j] + B[i][j]

print("MATRIZ SOMA:")
for i in range(0, m):
    for j in range(0, n):
        print(soma[i][j], end=" ")
    print()
