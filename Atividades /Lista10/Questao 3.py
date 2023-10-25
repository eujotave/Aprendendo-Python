print("Bem-vindo à Calculadora\nQual operação você deseja realizar?")
print("[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair")
escolha = int(input("Digite o número referente a sua escolha: "))

while escolha != 5:
    if escolha == 1:
        print("Você escolheu soma!")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"A soma dos números resultou em: {soma}\n")
        opcao = input("Deseja realizar outra operação? [S/N]: ")
        if opcao.upper() == "S":
            print("[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair")
            escolha = int(input("Digite o número referente a sua escolha: "))
        else:
            exit(0)
    if escolha == 2:
        print("Você escolheu subtração!")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        sub = num1 - num2
        print(f"A subtração dos números resultou em: {sub}\n")
        opcao = input("Deseja realizar outra operação? [S/N]: ")
        if opcao.upper() == "S":
            print("[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair")
            escolha = int(input("Digite o número referente a sua escolha: "))
        else:
            exit(0)
    if escolha == 3:
        print("Você escolheu multiplicação!")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        mult = num1 * num2
        print(f"A multiplicação dos números resultou em: {mult}\n")
        opcao = input("Deseja realizar outra operação? [S/N]: ")
        if opcao.upper() == "S":
            print("[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair")
            escolha = int(input("Digite o número referente a sua escolha: "))
        else:
            exit(0)
    if escolha == 4:
        print("Você escolheu divisão!")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        div = num1 / num2
        print(f"A divisão dos números resultou em: {div}\n")
        opcao = input("Deseja realizar outra operação? [S/N]: ")
        if opcao.upper() == "S":
            print("[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair")
            escolha = int(input("Digite o número referente a sua escolha: "))
        else:
            exit(0)
