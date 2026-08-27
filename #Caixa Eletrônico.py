#Caixa Eletrônico

#COM FUNÇÃO
def consulta_saldo(saldo):
    print(f"Seu saldo é: {saldo}")


def realiza_soma(saldo):
    valor_saque = float(input("Entre com o valor de saque: "))

    if valor_saque <= 0:
            print("Valor inválido!")
    elif valor_saque > saldo:
            print("Saldo insuficiente!")
    else:
            saldo = saldo - valor_saque
            print("Saquer realizado com sucesso!")
            return saldo

def realiza_deposito():
    if escolha == 3:
        valor_deposito = float(input("Entre com o valor a ser depositado!"))

        if valor_deposito > 0:
            saldo = saldo + valor_deposito
        else:
            print("Valor de depósito incorreto!")


def sistema_caixa():

saldo = 1500

escolha = 1

while escolha != 0:
    print("1 - Consulta Saldo")
    print("2 - Saída")
    print("3 - Depositar")
    print("4 - Sair")

    escolha = int(input("Entre com uma opção: "))

    if escolha == 1:
        print("Seu saldo é", saldo)
    
    elif escolha == 2:
        valor_saque = float(input("Entre com o valor de saque: "))

        if valor_saque <= 0:
            print("Valor inválido!")
        elif valor_saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo = saldo - valor_saque
            print("Saquer realizado com sucesso!")

    elif escolha == 3:
        valor_deposito = float(input("Entre com o valor a ser depositado!"))

        if valor_deposito > 0:
            saldo = saldo + valor_deposito
        else:
            print("Valor de depósito incorreto!")

    elif escolha == 0:
        print("Operação finalizada!")
    else:
        print("Opção incorreta. Tente novamente!")

sistema_caixa()


# SEM FUNÇÃO
saldo = 1500

escolha = 1

while escolha != 0:
    print("1 - Consulta Saldo")
    print("2 - Saída")
    print("3 - Depositar")
    print("4 - Sair")

    escolha = int(input("Entre com uma opção: "))

    if escolha == 1:
        print("Seu saldo é", saldo)
    
    elif escolha == 2:
        valor_saque = float(input("Entre com o valor de saque: "))

        if valor_saque <= 0:
            print("Valor inválido!")
        elif valor_saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo = saldo - valor_saque
            print("Saquer realizado com sucesso!")

    elif escolha == 3:
        valor_deposito = float(input("Entre com o valor a ser depositado!"))

        if valor_deposito > 0:
            saldo = saldo + valor_deposito
        else:
            print("Valor de depósito incorreto!")

    elif escolha == 0:
        print("Operação finalizada!")
    else:
        print("Opção incorreta. Tente novamente!")