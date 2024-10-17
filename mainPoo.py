'''from bibliotecaPoo import *
'''

try:
    lista = [1,2,3]
    print(lista[4])
except (IndexError, NameError, ):
    print("Teve um problema na lista")