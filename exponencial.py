def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return fatorial(n-1) #A função é executada dentro de si mesma



def exponencial(base, expoente):
    if base == 0:
        return 0
    elif expoente == 0:
        return 1
    else:
        return base*exponencial(base, expoente - 1)
    

num = int(input("Informe o número base: "))
expo = int(input("Informe o expoente: "))
resultado = exponencial(num, expo)

print(resultado)