lista = []
qtdd_numeros = int(input("Informe a quantidade de elementos da lista: "))
for num in range(qtdd_numeros):
    num = int(input("Informe o elemento a ser adicionado à lista: "))
    lista.append(num)
    lista.sort()
    print(lista)

pesquisa = int(input("Informe o número desejado: "))
for num in lista:
    if num == pesquisa:
        achado = lista.index(num)
        print(f"O número {pesquisa} foi achado na posição {achado}")   
    else:
        if pesquisa not in lista:
            print("O número não se encontra na lista.")