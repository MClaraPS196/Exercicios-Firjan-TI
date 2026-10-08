#Tempo corrida

def bubble_sort(tempo):
    for i in range(len(tempo)-1):
        for j in range(len(tempo)-1):
            if tempo[j] > tempo[j+1]:
                aux = tempo[j]
                tempo[j] = tempo[j+1]
                tempo[j+1] = aux
    return tempo

tempo = []

segundos = int(input("Informe o tempo, em segundos, que deseja adicionar ao sistema: "))
while segundos != 1:
    segundos = int(input("Informe o tempo, em segundos, que deseja adicionar ao sistema: "))
    tempo.append(segundos)

ordena = bubble_sort(tempo)
print(ordena)

procura = int(input("Informe o número que deseja buscar: "))
if procura in tempo:
    print(f"O tempo de {procura} segundos foi encontrado no sistema.")
else: 
    print("Tempo não registrado no sistema")
    