base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangolo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base ** 2 + altura ** 2) ** (1/2)

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")

