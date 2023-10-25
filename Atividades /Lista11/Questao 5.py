txt = input()

for carac in txt.upper():
    carac_repet = txt.count(carac)
    print(f"O caractere {carac} foi o que mais se repetiu, tendo o número de {carac_repet} ocorrências")
    break
