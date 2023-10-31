nome = str(input("Nome: "))
valor = float(input("Valor da hora: "))
hora = int(input("Horas trabalhadas: "))

salario = hora * valor

print(f"O pagamento para {nome} deve ser {salario:.2f}")
