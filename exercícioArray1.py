notas = [0]*5
tam = len(notas)
soma = 0
alunos = 0

for x in range (tam):
    notas[x] = float(input(f"Digite a {x+1}º nota: "))
for i in range (tam):
    soma = soma + notas[i]
media = soma/tam
for y in range(tam):
    if notas[y] > media:
        alunos += 1
print(f"A média da turma é {media} e {alunos} alunos ficaram com nota acima da média.")