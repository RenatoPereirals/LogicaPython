escala = str(input("Voce vai digitar a temperatura em qual escala (C/F)? "))

if escala == "F":
    tempera = float(input("Digite a temperatura em fahrenheit: "))
    C = 5 / 9 * (tempera - 32)
    print(f"Temperatura equivalente em Celsius: {C:.2f}")
else:
    tempera = float(input("Digite a temperatura em Celsius: "))
    F = 9 / 5 * tempera + 32
    print(f"Temperatura equivalente em fahrenheit: {F:.2f}")
