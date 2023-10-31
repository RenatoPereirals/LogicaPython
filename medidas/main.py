A = float(input("Digite a medida de A: "))
B = float(input("Digite a medida de B: "))
C = float(input("Digite a medida de C: "))

areaQuadrado = A * A
areaTriangulo = A * B / 2
areaTrapazio = (A + B) * C / 2

print(f"AREA DO QUADRADO = {areaQuadrado:.4f}")
print(f"AREA DO TRIANGULO = {areaTriangulo:.4f}")
print(f"AREA DO TRAPEZIO = {areaTrapazio:.4f}")
