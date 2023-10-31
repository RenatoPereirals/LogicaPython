a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a < b and a < c:
    menor = a
else:
    menor = min(b, c)

print(f"MENOR = {menor}")