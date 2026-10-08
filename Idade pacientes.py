# Idade pacientes

idades = []

idade = int(input("Informe a idade do paciente: "))
if idade > 0 and idade < 120:
    idades.append(idade)
    ordena = sorted(idades)

print(ordena)

procura = int(input("Informe a idade do paciente a ser buscada no sistema: "))
if procura in idades:
    print(f"Idade {procura} cadastrada no sistema!")
else:
    print("Idade do paciente não cadastrada no sistema")