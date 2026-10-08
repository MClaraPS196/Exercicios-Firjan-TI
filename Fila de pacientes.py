#Fila de pacientes

pacientes = []

quantos = int(input("Informe a quantidade de pacientes a serem cadastrados: "))
for num in range(quantos):
    nomes = input("Informe os nomes a serem cadastrados: ")
    pacientes.append(nomes)
    print(pacientes)

nomes_org = sorted(pacientes)
print(nomes_org)

pesquisa = input("Informe o nome do paciente que deseja buscar: ")
if pesquisa in pacientes:
    print(f"O nome {pesquisa} foi encontrado!")
else:
    print("Nome não encontrado na lista ou paciente não cadastrado no sistema.")