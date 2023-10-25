palavra = input("Digite uma palavra para ser invertida: ")
inverter = ""

for letra in range(len(palavra)-1, -1, -1):
    inverter += palavra[letra]

print(inverter)
