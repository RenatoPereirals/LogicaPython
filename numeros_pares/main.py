n = int(input("Quantos numeros voce vai digitar: "))

vet: [int] = [0 for x in range(0, n)]

for i in range(0, n):
    vet[i] = int(input("Digite um numero: "))

print()

cont = 0

print("Numeros pares:")
for i in range(0, n):
    if vet[i] % 2 == 0:
        print(vet[i], end=" ")
        cont += 1
print()
print()
print(f"Quantidade de pares = {cont}")
