salario = float(input("Digite o salario da pessoa: "))

novoSalario = 0

if salario <= 1000:
    novoSalario = salario * 1.20
elif salario <= 3000:
    novoSalario = salario * 1.15
elif salario <= 8000:
    novoSalario = salario * 1.1
elif salario > 8000:
    novoSalario = salario * 1.05

aumento = novoSalario - salario
porcentagem = aumento / salario * 100

print(f"Aumento = R$ {aumento:.2f}")
print(f"Porcentagem = {porcentagem:.0f} %")
