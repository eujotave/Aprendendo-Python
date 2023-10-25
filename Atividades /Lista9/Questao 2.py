palavra = input("Digite uma palavra: ")

cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

for carac in palavra.upper():
    if carac == "A":
        cont_a += 1
    elif carac == "E":
        cont_e += 1
    elif carac == "I":
        cont_i += 1
    elif carac == "O":
        cont_o += 1
    elif carac == "U":
        cont_u += 1

print(f"{cont_a} letra(s) A presentes na palavra")
print(f"{cont_e} letra(s) E presentes na palavra")
print(f"{cont_i} letra(s) I presentes na palavra")
print(f"{cont_o} letra(s) O presentes na palavra")
print(f"{cont_u} letra(s) U presentes na palavra")
