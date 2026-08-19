#Menu Simples
print("=====MENU=====")
print("Bem-vindo!")
print("Deseja fazer login ou cadastrar novo usuário?")

resposta = str(input("Digite a operação que deseja fazer: "))

if resposta == "login":
    print("=====PÁGINA DE LOGIN=====")
    login = str(input("Digite seu nome de usuário: "))
    senha = int(input("Digite sua senha: "))
    print(f"Bem-vindo, ", login, "!", "sua senha é: ", senha )
elif resposta == "cadastro":
    print("=====PÁGINA DE CADASTRO=====")
    Cadastro = str(input("Digite seu nome de usuário: "))
    senha = int(input("Crie uma senha numérica: "))
    confirma = str(input("Criar cadastro?"))
    if confirma == "sim":
        print("Cadastro criado com sucesso!")
    else:
        print("Cadastro Cancelado!")
    print("Bem-vindo, ", Cadastro, "!", "Sua senha é: ", senha, "!")
else:
    print("Operação Inválida!")