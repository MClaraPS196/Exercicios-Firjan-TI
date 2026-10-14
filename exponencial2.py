base = int(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))

def exponencial(base, expoente):
    if expoente == 0:
        return 1
    elif base == 0:
        return 0
    elif expoente == 1:
        return base
    else:
        return base*exponencial(base, expoente-1)
    
resultado = exponencial(base, expoente)
print(resultado)