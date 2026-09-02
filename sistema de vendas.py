def calcular_valor_vendas(quantidade, preco):
    return quantidade * preco 
 

def calcular_meta(valor_total):
    if valor_total >= 5000:
        return "Meta diária alcançada!"
    else:
        falta = 5000 - valor_total
        return f"Meta diária não alcançada. Faltam: {falta:.2f}"

def main():

    quantidade = 0
    valor_total = 0
    maior_venda = 0
    
    codigo_produto = int(input("Entre com o código do produto, e zero para encerrar o atendimento: "))

    while codigo_produto != 0:
        quantidade =int(input("Entre quantidade: "))
        preco = float(input("Entre com o preço: "))

        valor_vendas = calcular_valor_vendas(quantidade, preco)

        quantidade_vendas = quantidade_vendas + 1
        valor_total = valor_total + valor_vendas

        if valor_vendas > maior_venda:
            maior_venda = valor_vendas

        codigo_produto = int(input("Entre com o código do produto, ou zero para encerrar o atendimento: "))

    print("RELATÓRIO DE VENDAS")
    print("Quantidade de vendas realizadas: ", quantidade_vendas)
    print("O valor de vendas total: ", valor_total)
    print("Valor maior venda: ", maior_venda)

    meta = calcular_meta(valor_total)
    print(meta)


main()