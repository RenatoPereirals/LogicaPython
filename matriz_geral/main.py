n = int(input("Qual a ordem da matriz? "))

mat: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: "))

soma = 0

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] > 0:
            soma += mat[i][j]

print()
print(f"SOMA DOS POSITIVOS = {soma:.1f}")

print()
linha = int(input("Escolha uma linha: "))
print(f"LINHA ESCOLIDA: ", end="")
for j in range(0, n):
    print(f"{mat[linha][j]:.1f}", end=" ")

print()
print()
coluna = int(input("Escolha uma coluna: "))
print(f"LINHA ESCOLIDA: ", end="")
for i in range(0, n):
    print(f"{mat[i][coluna]:.1f}", end=" ")

print()
print()
print(f"DIAGONAL PRINCIPAL: ", end="")
for i in range(0, n):
    print(f"{mat[i][i]}", end=" ")

print()
print()
print("MATRIZ ALTERADA:")
for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            mat[i][j] = mat[i][j] ** 2
        print(f"{mat[i][j]:.1f}", end=" ")
    print()
