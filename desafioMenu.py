usuario = [""]*5
senha = [""]*5
tam = len(usuario)
menu = 0

while menu != 4:
    menu = int(input("Bem vindo! Digite a opção desejada: \n 1-Cadastro \n 2-Login \n 3-Mostrar usuários \n 4-Sair \n"))
    match menu:
        case 1:
            for x in range(tam):
                while True:
                    user = input(f"Digite o nome do {x+1}º usuário: ")

                    if user.strip() == "":
                        print("Usuário inválido. Tente novamente.")
                        continue

                    if user in usuario:
                        print("Usuário já cadastrado. Tente novamente.")
                        continue

                    password = input(f"Digite a senha do usuário {user}: ")

                    if password in senha:
                        print("Senha já cadastrada. Tente novamente.")
                        continue

                    if password.strip() == "":
                        print("Senha inválida. Tente novamente.")
                        continue

                    usuario[x] = user
                    senha[x] = password

                    break
            print("Cadastro realizado com sucesso!\n")

        case 2:

            tent = 3
            while tent > 0:
                tentUser = input(f"Digite o nome do usuário: ").strip()
                tentSenha = input(f"Digite a senha do usuário {tentUser}: ").strip()
                login = False

                for x in range(tam):
                    if usuario[x] == tentUser and senha[x] == tentSenha:
                        print("Login realizado com sucesso.\n")
                        login = True
                        break

                if login:
                    break

                else:
                    tent -= 1
                    print(f"Algo deu errado. Tente novamente. \nTentativas restantes: {tent}.\n")
            if tent <= 0:
                print("Acesso bloqueado. \nVocê excedeu o número de tentativas.")

        case 3:
            print("Usuários cadastrados: ")
            for x in range(tam):
                if usuario[x] and senha[x]:
                    print(f"Nome do usuário:{usuario[x]} \nSenha:{senha[x]} \nPosição:{x+1}\n")

        case 4:
            print("Saindo do sistema.")
            break

        case _:
            print("Opção inválida. Tente novamente.\n")