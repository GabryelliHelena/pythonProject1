'''Array guarda somente um tipo de dado

Lista pode ter tamanho 0, podendo aumentar/diminuir
Array tem que dizer qual o tamanho dele na criação, sem possibilidade de mudar

Vetor é um array unidimensional, tendo somente 1 linha
Para trabalhar matriz, tem que utilizar o For para travar na linha e outro For para trabalhar colunas

array é uma variável composta, tendo diversas variáveis simples dentro de um tamanho determidado
Deve atribuir um valor para a variável, dizendo o espaço onde vai ficar o valor
para que seja um array, o tamanho tem que ser no mínimo 2
Quando quer guardar mais de um valor do mesmo tipo
Deve indicar o tipo de dado a ser guardado no array. Ex: float N1=[15,12,10], string N1=[15,12,10]
Para mudar o valor em uma das posições, deve indicar a posição que se está alterando.
Ex.: Dado o array nomes = ['jose','joao','ana'], para mudar o valor de jose então nomes[0]=isa, assim o array original fica nomes = ['isa','joao','ana']

A melhor estrutura para ler o array é o For

Uma lista recebe qualquer tipo de dado, porém é mais lento na execução
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
