print("Digite dois numeros: ")
x = float(input())
y = float(input())

while x != y:
    if x > y:
        print("DECRESCENTE")
    else:
        print("CRESCENTE")

    print("Digite dois numeros: ")
    x = float(input())
    y = float(input())