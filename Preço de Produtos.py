#Preço de Produtos
def bubble_sort(precos):
    for i in range(len(precos)-1):
        for j in range(len(precos)-1):
            if precos[j] > precos[j+1]:
                aux = precos[j]
                precos[j] = precos[j+1]
                precos[j+1] = aux
    return precos

precos = []

quantos = int(input("Informe a quantidade de preços a serem adicionados: "))
for num in range(quantos):
    preco = int(input("Informe o preço a ser adicionado: "))
    precos.append(preco)
    print(precos)

ordena = bubble_sort(precos)
print(ordena)

pesquisa = int(input("Informe o número desejado: "))
if pesquisa in precos:
    print(f"O número {pesquisa} foi achado!")   
else:
        print("O número não se encontra na lista.")