n = int(input("Quantos alunos serao digitados: "))

nome: [str] = [0 for x in range(0, n)]
nota1: [float] = [0 for y in range(0, n)]
nota2: [float] = [0 for z in range(0, n)]

for i in range(0, n):
    print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno: ")
    nome[i] = str(input())
    nota1[i] = float(input())
    nota2[i] = float(input())

soma: [float] = [0 for w in range(0, n)]
media: [float] = [0 for k in range(0, n)]

for i in range(0, n):
    soma[i] = nota1[i] + nota2[i]
    media[i] = soma[i] / 2

print("Alunos aprovados:")

for i in range(0, n):
    if media[i] >= 6:
        print(nome[i])
