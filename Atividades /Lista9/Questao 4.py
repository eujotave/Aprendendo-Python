media_turma = 0
media_anual = 0
medias = []

for alunos in range(1, 41):
    media_anual = 0
    print(f"\nNotas do {alunos}° aluno \n")
    for media in range(1, 5):
        media_bim = float(input(f"Digite a {media}° média: "))
        media_anual += media_bim / 4
    medias.append(media_anual)
    media_turma = sum(medias) / 40

aluno = 1
print("")

for i in range(len(medias)):
    print(f"Média Anual do {aluno}° aluno: {medias[i]}")
    aluno += 1

print(f"\nMedia da turma: {media_turma}")
