idade = int(input("Digite as idades: "))

cont = 0
soma = 0

if idade < 0:
    print("IMPOSSIVEL CALCULAR")
else:
    while idade >= 0:
        soma += idade
        cont += 1
        idade = int(input("Digite as idades: "))

    media = soma / cont
    print(f"MEIDA = {media:.2f}")


