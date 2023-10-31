n = int(input("Quantos numeros voce vai digitar: "))

vet: [float] = [0 for x in range(0, n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

maior = vet[0]
posicao = 0

for i in range(0, n):
    if vet[i] > maior:
        maior = vet[i]
        posicao = i

print()
print(f"MAIOR VALOR = {maior:.1f}")
print(f"POSICAO DO MAIOR VALOR = {posicao}")
