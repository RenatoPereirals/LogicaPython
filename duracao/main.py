duracao = int(input("Digite a duração em segundos: "))

hora = duracao // 3600
minuto = duracao % 3600 // 60
segundo = duracao % 3600 % 60

print(f"{hora}:{minuto}:{segundo}")
