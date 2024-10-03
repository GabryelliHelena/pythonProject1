#Ler 10 números e guardar num vetor. Depois ler mais um número qualquer,
# contar e imprimir quantas vezes o número digitado aparece no array

numeros = [0]*10
tam = len(numeros)
cont = 0

for i in range (tam):
    numeros[i] = int(input(f"Digite o {i+1}º número: "))
num = int(input("Digite mais um número: "))
for j in range (tam):
    if num == numeros[j]:
        cont=cont+1
print(f"O número {num} aparece {cont} vezes no array.")