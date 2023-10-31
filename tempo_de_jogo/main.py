horaInicial = int(input("Hora inicial: "))
horaFinal = int(input("Hora final: "))

duracao = 24

if horaInicial > horaFinal:
    duracao = horaFinal - horaInicial + 24
elif horaFinal > horaInicial:
    duracao = horaFinal - horaInicial

print(f"O JOGO DUROU {duracao} HORA(S)")
