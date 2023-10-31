n = int(input("Quantos valores vai ter cade vetor: "))

A: [int] = [0 for x in range(0, n)]
B: [int] = [0 for y in range(0, n)]

print("Digite os valores do vetor A:")
for i in range(0, n):
    A[i] = int(input())

print("Digite os valores do vetor B:")
for i in range(0, n):
    B[i] = int(input())

C: [int] = [0 for z in range(0, n)]

print("VETOR RESULTANTE:")
for i in range(0, n):
    C[i] = A[i] + B[i]
    print(C[i])
