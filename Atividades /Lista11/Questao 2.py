num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

while num1 != 0 and num2 != 0:
    soma = num1 + num2
    print(f"A soma dos resultados foi: {soma}")
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    if num1 == 0 and num2 == 0:
        print("Operação Inválida")
        break
