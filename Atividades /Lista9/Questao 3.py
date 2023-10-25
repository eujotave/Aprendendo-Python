maior = 0
menor = 0
soma = 0
media = 0
numeros = []

for num in range(1, 31):
    numero = int(input(f"Digite o {num}° número: "))
    numeros.append(numero)
    maior = max(numeros)
    menor = min(numeros)
    soma = sum(numeros)
    media = soma / 30

print(f"{maior} é o maior número")
print(f"{menor} é o menor número")
print(f"{soma} é a soma de todos os números")
print(f"{media} é a media dos números informados")
