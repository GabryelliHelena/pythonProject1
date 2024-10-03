#Preencher um vetor A com 10 números

A = [0]*10
M = [0]*10
tam=len(A)
for x in range (tam):
    A[x] = int(input(f"Digite o {x+1}º número: "))
y = int(input("Digite o número multiplicador: "))
for i in range (tam):
    M[i] = y * A[i]
print(M)