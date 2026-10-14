def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return fatorial(n-1) #A função é executada dentro de si mesma

def exponencial(n, e):
    if n > 0 and e > 0:
        mult = n * n
        e = e - 1
        return mult
    return mult*exponencial(e-1)

num = int(input("Informe o número base: "))
expo = int(input("Informe o expoente: "))
resultado = exponencial(num, expo)

print(resultado)