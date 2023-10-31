n = int(input("Quantos elementos vai ter o vetor: "))

vet: [float] = [0 for x in range(0, n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

soma = 0

for i in range(0, n):
    soma += vet[i]

media = soma / n

print()
print(f"MEDIA DO VETOR = {media:.3f}")
print("ELEMENTOS ABAIXO DA MEDIA:")
for i in range(0, n):
    if vet[i] < media:
        print(f"{vet[i]:.1f}")
