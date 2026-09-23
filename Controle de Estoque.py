prod1 = 16
prod2 = 10
prod3 = 4
prod4 = 7
prod5 = 2
prod6 = 1
prod7 = 9
prod8 = 3
prod9 = 4
prod10 = 5
prod_menor5 = 0

prods = [prod1, prod2, prod3,prod4, prod5, prod6, prod7, prod8, prod9, prod10]

def total_prods(prod1,prod2, prod3,prod4, prod5, prod6, prod7, prod8, prod9, prod10):
    total = prod1 + prod2 + prod3 + prod4 + prod5+ prod6+ prod7+ prod8+ prod9 + prod10
    return total

def media():
    totall  = total_prods(prod1,prod2, prod3,prod4, prod5, prod6, prod7, prod8, prod9, prod10)
    media = totall/10
    return media

for prod in prods:
    print(f"Quantidade desse produto disponível: {prod}")
    if prod < 5:
        prod_menor5 += 1

maior = 0
for prod in prods: 
    if prod > maior:
        maior = prod
        print(f"Produto em maior quantidade disponível: {maior}")

total_produtos = total_prods(prod1,prod2, prod3,prod4, prod5, prod6, prod7, prod8, prod9, prod10)
print(f"Quantidade total de produtos no estoque: {total_produtos}")

mediaa = media()
print(f"Média de produtos: {mediaa}")

