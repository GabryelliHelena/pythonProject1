'''Array guarda somente um tipo de dado

Lista pode ter tamanho 0, podendo aumentar/diminuir
Array tem que dizer qual o tamanho dele na criação, sem possibilidade de mudar

Vetor é um array unidimensional, tendo somente 1 linha
Para trabalhar matriz, tem que utilizar o For para travar na linha e outro For para trabalhar colunas
'''

'''arrayCompras = ['banana','laranja','maçã']
for i in arrayCompras:
    print(i, end=' ')'''

'''import numpy as np

arrayNumeros = np.array([5,6,7,4,2,5])
tam = len(arrayNumeros)
for x in range(tam):
    print(arrayNumeros[x])'''

nomes = [0]*5
tam = len(nomes)

'''percorre o array e guarda novos dados'''
for x in range(tam):
    nomes[x] = input(f"Digite o {x + 1}º nome: ")

'''percorre o array e printar o índice e quem está dentro'''
for i in range (tam):
    print(i,nomes[i])
