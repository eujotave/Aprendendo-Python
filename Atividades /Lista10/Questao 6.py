count = 200

while count <= 300:
    ePrimo = True
    for i in range(2, count):
        if count % i == 0:
            ePrimo = False
            break
    if ePrimo:
        print(count)
    count += 1
