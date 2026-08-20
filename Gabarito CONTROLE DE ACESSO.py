# FUNÇÕES PARA LOGIN
def validacao(matricula_usuario, senha_usuario): #Recebe a matrícula e a senha do usuário
    return matricula_usuario == "138148" and senha_usuario == "1234" #Para ser validado, as credenciais devem bater com essas.


def login ():
    tentativas = 2 
    for  tentativa in range(1, tentativas+1):
        matricula_usuario = input("Entre com a matrícula: ")
        senha_usuario = input("Entre com a senha: ")

        if validacao(matricula_usuario, senha_usuario):
            print("Bem-vindo! Acesso Autorizado")
            return
        
        faltam = tentativas - tentativa
        print(f"Acesso negado, você ainda possui {faltam} tentativas.")

        if tentativas > 0:
            print("Suas tentativas acabaram. Tente Novamente mais tarde.")

login()