preco = float(input("Preço unitário do produto: "))
qtd = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

troco = dinheiro - qtd * preco

print(f"TROCO = {troco:.2f}")
