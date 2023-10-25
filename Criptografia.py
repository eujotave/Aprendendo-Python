import math

linhas = int(input())
letra = ""

for linhas in range(linhas):
    testes = (input())
    cripto = ""
    for letra in testes:
        if letra.isupper() or letra.islower():
            n_letra = ord(letra) + 3
            n_letra = chr(n_letra)
        else:
            n_letra = letra
        cripto += n_letra
    cripto = cripto[::-1]
    metade_str = math.floor(len(cripto) // 2)
    cripto = list(cripto)
    for carac in range(metade_str, len(cripto)):
        n_carac = ord(cripto[carac]) - 1
        cripto[carac] = chr(n_carac)

    cripto = "".join(cripto)

    print(cripto)
