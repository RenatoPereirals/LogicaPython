preco = float(input("Preco unitario: "))
qtd = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinhiero recebido: "))

troco = dinheiro - (qtd * preco)

if troco < 0:
    print(f"DINHEIRO INSUFICIENTE. FALTAM {abs(troco):.2f} REAIS")
else:
    print(f"TROCO = {troco:.2f}")
