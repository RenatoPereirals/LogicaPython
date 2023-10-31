codigo = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

contAlcool = 0
contGasolina = 0
contDisel = 0

while codigo != 4:
    if codigo == 1:
        contAlcool += 1
    elif codigo == 2:
        contGasolina += 1
    elif codigo == 3:
        contDisel += 1

    codigo = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

print("MUITO OBRIGADO")
print(f"Alcool: {contAlcool}")
print(f"Gasolina: {contGasolina}")
print(f"Disel: {contDisel}")
