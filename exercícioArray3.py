#Leia 5 números e armazene em um vetor depois print na ordem inversa.

numeros = [0]*5
tam = len(numeros)

for i in range (tam):
    numeros[i] = int(input(f"Digite o {i+1}º número: "))
for x in range (tam-1,-1,-1):
    print(numeros[x], end=" ")