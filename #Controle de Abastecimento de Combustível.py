#CONTROLE DE ABASTECIMENTO DE COMBUSTÍVEL
veiculos_mais40litros = 0
quantidade_veiculos = []
quantidade_litros = 0
preco_litro = 5
valor_total = 0


print("===== SISTEMA DO POSTO DE GASOLINA =====")

estaciona = str(input("Deseja estacionar para abastecer seu veículo?"))
if estaciona != "sim":
    print("Ok, siga em frente e tenha uma boa viagem!")
else:
    quantidade_total_veiculos = quantidade_veiculos + 1
    
    abastece = int(input("Informe a quantidade de litros que deseja abastecer seu carro: "))
    if abastece == 0:
        print("É necessário escolher no mínimo 1 litro para abastecer!")
    else:
        quantidade_litros_total = quantidade_litros + abastece
        valor_abastecimento = quantidade_litros_total * preco_litro
        valor_a_pagar = valor_total + valor_abastecimento
        for i in quantidade_veiculos:
            media_litros = quantidade_litros_total/quantidade_veiculos[i]

        
    print(f"Quantidade de veículos abastecidos: {quantidade_total_veiculos}")
    print(f"Quantidade de litros vendidos: {quantidade_litros_total}")
    print(f"Valor total das vendas: {valor_a_pagar}")
    print(f"A média de litros abastecidos foi: {media_litros}")

