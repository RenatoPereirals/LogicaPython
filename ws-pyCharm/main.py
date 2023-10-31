largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do terreno: "))

area = largura * comprimento
preco = valor * area

print(f"Area do terreno {area:.2f}")
print(f"Valor do terreno {preco:.2f}")