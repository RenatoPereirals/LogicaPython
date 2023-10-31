nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

soma = nota1 + nota2
print(f"NOTA FINAL = {soma}")
if soma < 60:
    print("REPROVADO")