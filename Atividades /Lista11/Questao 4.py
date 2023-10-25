txt1 = input()
txt2 = input()

encontrar = False

for t in range(len(txt1), 0, -1):
    for i in range(len(txt1) - t + 1):
        sub = txt1[i:i+t]
        if sub in txt2:
            print(sub)
            print(len(sub))
            encontrar = True
            break
    if encontrar:
        break
