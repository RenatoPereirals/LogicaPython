duracao = int(input("Digite a quantidade de minutos: "))

if duracao < 100:
    valor = 50
else:
    valor = (duracao - 100) * 2 + 50

print(f"Valor a pagar = R$ {valor:.2f}")
