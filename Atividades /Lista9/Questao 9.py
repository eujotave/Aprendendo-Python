molecula = input("Digite uma fita DNA: ")
n_molecula = ""

for bases in molecula.upper():
    n_molecula = molecula.replace("T", "U")

print(f"{n_molecula} é a molécula RNA correspondente")
