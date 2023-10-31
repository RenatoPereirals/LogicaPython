n = int(input("Serao digitados dados de quantos produtos: "))

nome: [str] = [0 for x in range(0, n)]
precoCompra: [float] = [0 for y in range(0, n)]
precoVenda: [float] = [0 for z in range(0, n)]

for i in range(0, n):
    print(f"Produto {i + 1}")
    nome[i] = str(input("Nome: "))
    precoCompra[i] = float(input("Preco de compra: "))
    precoVenda[i] = float(input("Preco de venda: "))

abaixo = 0
entre = 0
acima = 0

for i in range(0, n):
    lucro = (precoVenda[i] - precoCompra[i]) / precoCompra[i] * 100
    if lucro < 10:
        abaixo += 1
    elif lucro < 20:
        entre += 1
    else:
        acima += 1

totalCompra = 0
totalVenda = 0

for i in range(0, n):
    totalCompra += precoCompra[i]
    totalVenda += precoVenda[i]

totalLucro = totalVenda - totalCompra

print()
print("RELATORIO:")
print(f"Lucro abaixo de 10%: {abaixo}")
print(f"Lucro entre 10% e 20%: {entre}")
print(f"Lucro acima de 20%: {acima}")

print(f"Valor total de compra: {totalCompra:.2f}")
print(f"Valor total de venda: {totalVenda:.2f}")
print(f"Lucro total: {totalLucro:.2f}")
