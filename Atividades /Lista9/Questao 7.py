sequen = input("Digite a sequência de resultados: ")
pontos = 0

for resul in sequen.upper():
    if resul == "V":
        pontos += 3
    elif resul == "E":
        pontos += 1
    elif resul == "D":
        pontos += 0

print(f"O time fez {pontos} pontos")
