def analise_de_vendas():
    total = 0
    media = 0 
    acima100 = 0
    maior_venda = 0
    menor_venda = 0
    n = 0

    n = int(input("Digite a quantidade de vendas: "))
    for i in range(n):
        venda = float(input("Digite o valor da compra: "))
        total += venda
        media = total/n

        if venda > 100:
            acima100 += 1

        if venda > maior_venda:
            maior_venda = venda 
        
        if menor_venda == 0 or venda < menor_venda:
            menor_venda = venda

    print(f"O total do dia foi R${total:.2f}")
    print(f"A média de valores foi R$ {media:.2f}")
    print(f"O maior valor de venda é R$ {maior_venda:.2f}")
    print(f"A menor valor de venda é R$ {menor_venda:.2f}")
    print(f"{acima100} vendas foram acima de R$100")

analise_de_vendas()