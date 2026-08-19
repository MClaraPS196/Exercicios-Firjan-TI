
#Gabarito

quantidade = 0
total = 0.0

def media_precos():
    if quantidade >0:
        return total/quantidade
    
def funcao_principal():
    print("Quantidade: ", quantidade)
    print("Valor: ", total)
    print("Média: ", media)

preco = float(input("Entre com o preço do produto: "))

while preco != 0:
    total = total + preco
    quantidade = quantidade + 1
    preco = float(input("Entre com o preço: "))

media = total / quantidade

print(f'Valor total: {total}')
print(f'Valor média: {media}')


