palavra = input("Digite uma palavra: ")
inverter = ""

for letra in range(len(palavra)-1, -1, -1):
    inverter += palavra[letra]

if inverter.upper() == palavra.upper():
    print("É palíndromo")
else:
    print("Não é palíndromo")
