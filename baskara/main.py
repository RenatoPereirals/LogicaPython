a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b * b - 4 * a * c

if delta < 0 or a == 0:
    print("Esta equacao nao possui raizes reais")
else:
    x1 = (-b + delta ** (1/2)) / (2 * a)
    x2 = (-b - delta ** (1/2)) / (2 * a)
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")
