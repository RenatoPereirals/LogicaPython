codigo = int(input("Codigo do produto comprado: "))
qtd = int(input("Quantidade comprada: "))

valor = 0
if codigo == 1:
    valor = 5
elif codigo == 2:
    valor = 3.5
elif codigo == 3:
    valor = 4.8
elif codigo == 4:
    valor = 8.9
elif codigo == 5:
    valor = 7.32

preco = valor * qtd
print(f"Valor a pagar: R$ {preco:.2f}")
