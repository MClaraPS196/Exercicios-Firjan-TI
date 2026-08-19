#Controle de Acesso
# Uma empresa possio um sistemad de controle de acesso. Para entrar, o funcionário precisa informar matrícula e senha.
# O sistema possui apenas 3 tentativas. Se os dados estiverem corretos, deve apresentar "Acesso Autorizado". Caso contrário,
# Deve informar quantas tentativas ainsa estão disponíveis. Após três tentativas incorretas, o sistema deve apresentar
# "Usuário Bloqueado".
#Responda: Qual é a condição para permitir o acesso? O que precisa ser contado?
# Qual estrutura de repetição você utilizaria? O que acontece quando o usuário acerta a senha antes da terceira tentativa.

#Funcionario informa matricula e senha
print("==========SISTEMA PRINCIPAL DA EMPRESA==========")
matricula = int(input("Informe seu número de matrícula:"))
if len(matricula) < 8:
    print("Nome de Usuário inválido.")
senha = str(input("Informe sua senha: "))
if len(senha) <8:
    print("Senha inválida.")

    ##

if len(matricula) != 12 or len(senha) < 8:
    for tentativa in range(1,3):
        i = tentativa - 1
        print(f"Credencial Inválida. Você possui mais {tentativa[i]} tentativas")
        if tentativa[i] == 0:
            print("Usuario Bloqueado. Tente Novamente mais tarde.")
else:
    print("Acesso Autorizado. Bem-vindo!")
