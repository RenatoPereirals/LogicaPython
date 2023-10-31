n = int(input("Qual a ordem da matriz? "))

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0,n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

maiorLinha: [int] = [0 for x in range(n)]
maiorLinha[i] = mat[0][0]

for i in range(0, n):
    for j in range(0,n):
        if mat[i][j] > maiorLinha[i]:
            maiorLinha[i] = mat[i][j]

print("MAIOR ELEMENTO DE CADA LINHA: ")
for i in range(0, n):
    print(maiorLinha[i])
