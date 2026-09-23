#Controle de Temperaturas

dia1 = int(input("Informe a temperatura do dia: "))
dia2 = int(input("Informe a temperatura do dia: "))
dia3 = int(input("Informe a temperatura do dia: "))
dia4 = int(input("Informe a temperatura do dia: "))
dia5 = int(input("Informe a temperatura do dia: "))
dia6 = int(input("Informe a temperatura do dia: "))
dia7 = int(input("Informe a temperatura do dia: "))
dia_acima30 = 0

dias = [dia1, dia2, dia3, dia4, dia5, dia6, dia7]

def media(dia1, dia2, dia3, dia4, dia5, dia6, dia7):
    total = dia1 + dia2 + dia3 + dia4 + dia5 + dia6 + dia7
    media = total/7
    return media


for dia in dias:
    print(f"Temperatura registrada no dia {dias.index(dia)}: {dia}")
    
    maior_valor = dias[0]
    if maior_valor < dia:
        maior_valor = dia

    menor_valor = dias[0]
    if menor_valor > dia:
        menor_valor = dia

    if dia > 30:
        dia_acima30 += 1


mediaa = media(dia1, dia2, dia3, dia4, dia5, dia6, dia7)
print(f"Média das temperaturas: {mediaa:.1f}")
print(f"Maior temperatura: {maior_valor}")
print(f"Menor temperatura: {menor_valor}")
print(f"Dias em que a temperatura foi acima de 30: {dia_acima30}")