#Cobra_Estacionamento
#Um estacionamento cobra: ATé 1 hora: R$8,00; de 1 até 3 horas: R$15,00; acima de 3 horas: R$20,00.
#O sistema deve receber a quantidade de horas que cada veículo permaneceu no estacionamento e calcular o valor a pagar.
#O operador continuará registrando veículos até informar 0. Ao final, apresentar quantidade de ceículos, valor total arrecadao e quantidade de veículos que permaneceram
# mais de 3 horas.

quantidade = 0
total = 0
veiculo_acima_3h = 0

horas = float(input("Informe a quantidade de horas que o carro ficará no estacionamento: "))

while horas != 0:
    if horas <=1:
        preco = 8
    elif horas <= 3:
        preco = 15
    else:
        preco = 20
        veiculo_acima_3h = veiculo_acima_3h + 1
    
    quantidade = quantidade + 1
    total = total + preco

    horas = float(input("Informe a quantidade de horas que o carro ficará no estacionamento: "))

print(f"Quantidade: {quantidade}, total: {total}")
print(f"Carros que ficaram mais de 3h: {veiculo_acima_3h}")