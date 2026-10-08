# Estoque 

def bubble_sort(unidades):
    for i in range(len(unidades)-1):
        for j in range(len(unidades)-1):
            if unidades[j] > unidades[j+1]:
                aux = unidades[j]
                unidades[j] = unidades[j+1]
                unidades[j+1] = aux
    return unidades


unidades = []

quantos = int(input("Informe quantos tipos de produtos serão adicionados ao sistema: "))
for num in range(quantos):
    unidade = int(input("informe a quantidade de unidades deste produto a serem adicionadas ao sistema: "))
    unidades.append(unidade)

ordena = bubble_sort(unidades)
print(ordena)

procura = int(input("Informe a quantidade que deseja verificar no sistema: "))
if procura in unidades:
    print(f"Quantidade {procura} cadastrada no sistema!")
else:
    print("Quantidade não cadastrada no sistema.")