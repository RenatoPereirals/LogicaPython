a = int(input("Digite um numero: "))

while a != 0:

    if a % 2 == 0:
        soma = 5 * a + 20
    else:
        soma = 5 * a + 25

    print(f"SOMA = {soma}")
    a = int(input("Digite um numero: "))