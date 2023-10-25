num = int(input("Digite um número: "))

while num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Não é primo")
            exit(0)
    else:
        print("É primo")
        exit(0)

if num == 0:
    print("É zero")
elif num == 1:
    print("Por definição, 1 não é primo")
else:
    print("É negativo")
