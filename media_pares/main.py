n = int(input("Quantos elementos vai ter o vetor: "))

vet: [int] = [0 for x in range(0, n)]

for i in range(0, n):
    vet[i] = int(input("Digite um numero: "))

contPares = 0
somaPares = 0

for i in range(0, n):
    if vet[i] % 2 == 0:
        somaPares += vet[i]
        contPares += 1
if contPares == 0:
    print("NENHUM NUMERO PAR")
else:
    mediaPares = somaPares / contPares
    print(f"MEDIA DOS PARES = {mediaPares:.1f}")
