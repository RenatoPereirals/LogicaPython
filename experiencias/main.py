n = int(input("Quantos casos serao digitados: "))

contCoelho = 0
contRato = 0
contSapo = 0

for i in range(0, n):

    qtdCobaias = int(input("Quantidade de cobaias: "))
    tipoCobaia = str(input("Tipo de cobaia: "))

    if tipoCobaia == 'C':
        contCoelho += qtdCobaias
    elif tipoCobaia == 'R':
        contRato += qtdCobaias
    elif tipoCobaia == 'S':
        contSapo += qtdCobaias

totalCobaias = contCoelho + contSapo + contRato

pCoelho = contCoelho / totalCobaias * 100
pRato = contRato / totalCobaias * 100
pSapo = contSapo / totalCobaias * 100

print()
print("RELATORIO FINAL")

print(f"Total: {totalCobaias} cobaias")
print(f"Total de coelhos: {contCoelho}")
print(f"Total de ratos: {contRato}")
print(f"Total de sapos: {contSapo}")

print(f"Percentual de coelhos: {pCoelho:.2f}")
print(f"Percentual de ratos: {pRato:.2f}")
print(f"Percentual de sapos: {pSapo:.2f}")
