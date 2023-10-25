palavra = input("Digite uma palavra: ")
cont_b = 0
cont_c = 0
cont_d = 0

for carac in palavra.upper():
    if carac == "B":
        cont_b += 1
    elif carac == "C":
        cont_c += 1
    elif carac == "D":
        cont_d += 1

print(f"{cont_b} letra(s) B presentes na palavra")
print(f"{cont_c} letra(s) C presentes na palavra")
print(f"{cont_d} letra(s) D presentes na palavra")
