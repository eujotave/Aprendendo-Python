molecula = input("Digite uma fita DNA: ")
m_complementar = ""
nova_base = ""

for b in range(len(molecula) - 1, -1, -1):
    m_complementar += molecula[b]

for bases in m_complementar.upper():
    if bases == "A":
        bases_nova = "T"
        nova_base += bases_nova
    elif bases == "T":
        bases_nova = "A"
        nova_base += bases_nova
    elif bases == "G":
        bases_nova = "C"
        nova_base += bases_nova
    elif bases == "C":
        bases_nova = "G"
        nova_base += bases_nova

print(f"{nova_base} é o complemento reverso dela")
