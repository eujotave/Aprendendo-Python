# Nome

nome = str(input("Digite seu nome:"))
while len(nome) <= 3:
    print("O nome tem que ter no mínimo 3 caracteres")
    nome = str(input("Digite seu nome:"))

# Idade

idade = int(input("Digite sua idade:"))
while idade < 0 or idade > 150:
    print("Esta não é uma idade válida")
    idade = int(input("Digite sua idade:"))

# Salário

salario = float(input("Digite seu salário:"))
while salario < 0:
    print("Este não é um número válido")
    salario = float(input("Digite seu salário:"))

# Sexo
sexo = str(input("Digite seu sexo [m = masculino | f = feminino]:"))
while (sexo != "m") and (sexo != "f"):
    print("Este não é um sexo válido")
    sexo = str(input("Digite seu sexo [m = masculino | f = feminino]:"))

# Estado Civil

est_civil = str(input("Digite seu estado civil \n [s = solteiro]:\n [c = casado]\n [v = viúvo]\n "
                      "[d = divórciado]:\n"))
while (est_civil != "s") and (est_civil != "c") and (est_civil != "v") and (est_civil != "d"):
    print("Este não é um estado civil válido")
    est_civil = str(input("Digite seu estado civil \n [s = solteiro]:\n [c = casado]\n [v = viúvo]\n "
                          "[d = divórciado]:\n"))
print("Informações coletadas com sucesso")











