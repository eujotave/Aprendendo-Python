count = 0
num = 2

while count <= 100:
    ePrimo = True
    for i in range(2, num):
        if num % i == 0:
            ePrimo = False
            break
    if ePrimo:
        print(num)
        count += 1
    num += 1
