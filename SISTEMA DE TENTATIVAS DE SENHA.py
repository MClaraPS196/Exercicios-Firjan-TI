# SISTEMA DE TENTATIVAS DE SENHA
tentativas = 4
senha = "Python@2026"

senha_usu = input("Informe a senha: ")
if senha_usu == senha:
    print("Acesso Liberado!")
else: 
    if senha_usu != senha:
        for i in range(tentativas):
            print("Erro inesperado. Tente Novamente!")
            senha_usu = input("Informe a senha: ")
            if senha_usu == senha:
                print("Acesso Liberado!")
                break
            else:
                print("Erro inesperado. Tente Novamente!")
                tentativas -= 1
                if tentativas == 0:
                    print("Acesso Bloqueado!")
