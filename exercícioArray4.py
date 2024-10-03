#Ler 5 nomes de usuários e suas senhas. Armazenar cada lista em um array diferente.
# Imprimir nome, senha e posição no array.

nomes = [""]*5
senhas = [0]*5
tam = len(nomes)

for i in range (tam): #cadastro
    nomes[i] = input(f"Digite o {i+1}º usuário: ")
    senhas[i] = int(input(f"Digite a senha de {nomes[i]}: "))
for j in range (tam):
    print(nomes[j],senhas[j],j) #digitou2- motrar user cadastrado (user, senha e posição)

#login = olhar a posição em que o valor está e tem que correspondente. Se user/senha errada, mostrar msgm
#digitar 4 - sair do sistema
#3 tentativas totais