from bibliotecaPoo import *

while True:
    opcao = int(input("Digite a opção desejada.\n"
                      "1 - INSERIR\n"
                      "2 - MOSTRAR\n"
                      "3 - SAIR\n"
                      "4 - PESQUISAR\n"))
    match opcao:
        case 1:
            cadastrar(input("Digite um texto para cadastrar: "))
        case 2:
            mostrar()
        case 3:
            break
        case 4:
            pesquisar(input("Digite o texto para pesquisar: "))
        case _:
            print("Opção inválida.")