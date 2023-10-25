botas_indiv = int(input("Digite o número de botas: "))
tamanho_comp = []
pe = ""
tamanho_direito = []
tamanho_esquerdo = []
par = 0

for botas in range(botas_indiv):
    tamanho, pe = input().split()
    tamanho = int(tamanho)
    pe = str(pe)
    if pe == "D":
        tamanho_direito.append(tamanho)
    elif pe == "E":
        tamanho_esquerdo.append(tamanho)
    if tamanho in tamanho_esquerdo and tamanho in tamanho_direito:
        par += 1

if par == 0:
    print("Nenhum par de botas pode ser formado")
    exit(0)

print(f"{par} pares de botas podem ser formados")
