def minha_funcao():
    return "oi"

teste = minha_funcao()
print(teste)


def media(a,b,c,d):
    soma = (a+b+c)//d #Se colocar a+b+c/d, só o valor de c será dividido por d. Para dividir tudo, depe colocar as demais vars em ().
    return soma

a = 10
b = 10
c = 10
d = 3

somei = media(10,10,10,3)
print(somei)


