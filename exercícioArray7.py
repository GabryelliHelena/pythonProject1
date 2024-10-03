#Leia 10 valores inteiros e armazene num vetor. O algoritmo deve informar:
#1)todos os números pares 2)o menor e maior valor 3)quantos dos valores são maiores que a média desses valores

numeros = [0]*4
tam = len(numeros)
pares = [0]*4
maior = 0
menor = 0
soma = 0
media = 0
cont = 0

for i in range (tam):
    numeros[i] = int(input(f"Digite o {i+1}º número: "))

for j in range (tam):
    if (numeros[j] % 2) == 0:
        pares[j] =  numeros[j]

for k in range (tam):
    maior = max(numeros)
    #o cálculo lógico para a função max é abrir um if comparando o array com a variável maior:
    #if numeros[k] > maior:
        #maior = numeros[k]

for l in range (tam):
    menor = min(numeros)

for m in range (tam):
    soma = soma + numeros[m]

media = soma / tam

for n in range (tam):
    if numeros[n] > media:
        cont+=1

for p in range (tam):
    print(f"Números pares: {pares[p]}. O maior: {maior}. O menor: {menor}. A média: {media}. Qtos acima da média: {cont}")
