
def calcular_consumo():

    total = 0
    maior = 0
    menor = 0
    mes_maior = 0

    for mes in range(1,13): # Vai do mês 1 ao 12
        consumo_mensal = float(input(f"Digite o consumo do mês: {mes}"))

        total = total + consumo_mensal

        if mes == 1:
            maior = consumo_mensal
            menor = consumo_mensal
            mes_maior = mes
        else:
            if consumo_mensal > maior:
                maior = consumo_mensal
                mes_maior = mes
            if consumo_mensal < menor: # IF duplo para serem executados ao mesmo tempo
                menor = consumo_mensal

    media =  total/12

    print("\n--- RESULTADO ---")
    print("Relatório de gastos mensais")
    print(f"Consumo total: {total}")
    print(f"A média de gastos foi: {media:.2f}")
    print(f"O maior consumo foi: {maior} e o menor: {menor}")

calcular_consumo()