#é um pedaço de código que escreve para usar o mesmo código várias vezes
#a função só é executada quando é chamada em outro arquivo
#o asterisco antes de qualquer variável indica que recebe qualquer quantidade de valores, sendo sempre uma tupla
#tupla é uma lista imutável, recebendo um valor sem conseguir alterar. Para manipular, tem que usar o For.

def somar(num1,num2,num3,num4,num5):
    soma = num1+num2+num3+num4+num5
    print(soma)

def soma(*numeros):
    soma = 0
    for x in numeros:
        soma = soma + x
    print(soma)

'''def texto(letras):
    qtd = 0
    tam = len(letras[0])
    for x in letras[0]:
        if x != " ":
            qtd+=1
    print(qtd)
    for i in range(tam-1,-1,-1):
        print(letras[0][i],end='')'''

#outra forma de resolver

def texto(letras):
    qtd = 0
    for x in letras:
        if x not in " ":
            qtd += 1
    print(qtd)

    print(letras[::-1]) #outra forma de printar ao contrário é usando slice, com dois pontos duas vezes ::
'''    tam = len(letras)
    for z in range (tam-1,-1,-1):
        print(letras[z], end=" ")''' #forma tradicional
