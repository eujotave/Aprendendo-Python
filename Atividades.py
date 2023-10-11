hi, mi, hf, mf = map(int, input().split())

mi += hi * 60
mf += hf * 60

tempo = mf - mi

if tempo <= 0:
    tempo += 24*60

horas = tempo // 60
minutos = tempo % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
