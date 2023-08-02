print("Seja bem-vindo ao nosso programa, você poderá informar uma quantidade inderteminada de valores.\n"
      "Quando quiser para o programa, é só digitar -1")

valor = 0
valores = []
quantidade = 0
soma = 0
media = 0
aprovados = 0
reprovados = 0

while valor != -1:
    valor = float(input("Digite o próximo valor:"))
    valores.append(valor)
    quantidade += 1
    soma = soma + valor
    if valor >= 7:
        aprovados += 1
    else:
        reprovados += 1
    if valor == -1:
        soma += 1
        final = quantidade - 1
        media = soma / final


valores.pop(-1)
print(quantidade - 1)
print(valores)
valores.reverse()
for elemento in valores:
    print("->", elemento)
print(soma)
print(media)
print(f"A quantidade de valores acima da média foi {aprovados}")
print(f"A quantidade de valores abaixo da média foi {reprovados - 1}")
print("\nPrograma encerrado\n")