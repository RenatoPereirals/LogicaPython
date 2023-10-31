n = int(input("Quantas pessoas serao digitadas: "))

genero: [str] = [0 for x in range(0, n)]
altura: [float] = [0 for y in range(0, n)]

for i in range(0, n):
    altura[i] = float(input(f"Altura da {i+1}a pessao: "))
    genero[i] = str(input(f"Genero da {i+1}a pessao: "))

menor = altura[0]
maior = altura[0]

for i in range(0, n):
    if altura[i] > maior:
        maior = altura[i]
    elif altura[i] < menor:
        menor = altura[i]

somaMulheres = 0
contMulheres = 0

for i in range(0, n):
    if genero[i] == 'F':
        somaMulheres += altura[i]
        contMulheres += 1

media = somaMulheres / contMulheres
numHomem = n - contMulheres

print(f"Menor altura: {menor:.2f}")
print(f"Maior altura: {maior:.2f}")
print(f"Media das alturas das mulheres: {media:.2f}")
print(f"Numero de homens: {numHomem}")
