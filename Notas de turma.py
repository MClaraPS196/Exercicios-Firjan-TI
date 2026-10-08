#Notas de turma

def bubble_sort(notas):
    for i in range(len(notas)-1):
        for j in range(len(notas)-1):
            if notas[j] > notas[j+1]:
                aux = notas[j]
                notas[j] = notas[j+1]
                notas[j+1] = aux
    return notas

notas =[]

quantas = int(input("Informe quantas notas serão adicionadas ao sistema: "))
for num in range(quantas):
    nota = int(input("Informe a nota a ser adicionada na lista: "))
    notas.append(nota)

ordena = bubble_sort(notas)
print(ordena)

pesquisa = int(input("Informe a nota a ser buscada: "))
if pesquisa in notas:
    print(f"Nota {pesquisa} encontrada no sistema!")
else:
    print("Nota não registrada no sistema.")