print("As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores")
salario = float(input("Qual o salário atual do colaborador:"))

if 0 <= salario <= 280:
    aumento = (salario / 100) * 20
    print(f"O salário antes do reajuste era {salario}. Com o reajuste de 20% (ou seja {aumento:.2f}), o salário "
          f"ficou {salario + aumento:.2f}")
elif 280 < salario <= 700:
    aumento = (salario / 100) * 15
    print(f"O salário antes do reajuste era {salario}. Com o reajuste de 15% (ou seja {aumento:.2f}), o salário "
          f"ficou {salario + aumento:.2f}")
elif 700 < salario <= 1500:
    aumento = (salario / 100) * 10
    print(f"O salário antes do reajuste era {salario}. Com o reajuste de 10% (ou seja {aumento:.2f}), o salário "
          f"ficou {salario + aumento:.2f}")
elif salario > 1500:
    aumento = (salario / 100) * 5
    print(f"O salário antes do reajuste era {salario}. Com o reajuste de 5% (ou seja {aumento:.2f}), o salário "
          f"ficou {salario + aumento:.2f}")
else:
    print("O colaborar tá desempregado XD")

