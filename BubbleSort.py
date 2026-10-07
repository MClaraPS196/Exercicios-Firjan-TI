def bubble_sort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

lista = []
qtdd_numeros = int(input("Informe a quantidade de elementos da lista: "))
for num in range(qtdd_numeros):
    num = int(input("Informe o elemento a ser adicionado à lista: "))
    lista.append(num)
    print(lista)

bolha = bubble_sort(lista)
print(bolha)

pesquisa = int(input("Informe o número desejado: "))
for num in lista:
    if num == pesquisa:
        achado = lista.index(num)
        print(f"O número {pesquisa} foi achado na posição {achado}")   
    else:
        if pesquisa not in lista:
            print("O número não se encontra na lista.")