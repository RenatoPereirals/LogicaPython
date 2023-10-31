print("Digite dois numeros inteiros:")
a = int(input())
b = int(input())

if a < b:
    troca = a
    a = b
    b = troca

if a % b == 0:
    print("São multiplos")
else:
    print("Não são multiplos")
