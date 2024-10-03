#Leia 5 nomes e print esses nomes na ordem normal sendo na horizontal e inversa sendo um por linha

nomes = [""]*5
nomesInvert = [""]*5
tam = len(nomes)

for i in range (tam):
    nomes[i] = input(f"Digite o {i+1}º nome: ")
for j in range (tam):
    print(nomes[j], end=" ")
print()
for k in range (tam-1,-1,-1):
    print(nomes[k])