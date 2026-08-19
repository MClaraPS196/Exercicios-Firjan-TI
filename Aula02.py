def soma(a,b):
    return a + b
resultado = soma(25, 10)
print(resultado)


def diminui(a,b):
    return a - b
resultado1 = diminui(12,7)
print(resultado1)


def multiplica(a, b):
    return a * b
resultado2 = multiplica(7, 4)
print(resultado2)


def divide(a, b):
    return a/b
resultado3 = divide(20,3)
print(resultado3)

#JEITO ALTERNATIVO# 
def soma(a,b):
    return a+b

def subtrai(a,b):
    return a-b

def multiplica(a,b):
    return a*b

def divide(a,b):
    if b != 0:
        return a/b
    else:
        print("Não é possível dividir por zero")

a = float(input("Informe o valor de a:"))
b = float(input("Informe o valor de b:"))

print("Enter ")


resultado = soma(45, 31)
print(resultado)
resultado1 = subtrai(32, 17)
print(resultado1)
resultado2 = multiplica(76, 43)
print(resultado2)
resultado3 = divide(87, 56)
print(resultado3)