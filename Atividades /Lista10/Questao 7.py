n = int(input("Digite um número: "))
num = 0
triangular = (num * (num + 1) * (num + 2))

while triangular < n:
    triangular = (num * (num + 1) * (num + 2))
    num += 1

if n == triangular:
    print("É triangular")
else:
    print("Não é triangular")
