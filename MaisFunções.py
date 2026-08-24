def minha_funcao():
    a = 0
    b = 2
    soma = a + b
    print(soma)

# minha_funcao()

def informacoes_tp(**informacoes):
    for chave, valor in informacoes.item():
        print(f"{chave}:{valor}")

#informacoes_tp(nome="Lan Code", idade = 20, inscritos = 20000, videos=45)


def contagem_regressiva(numero):
    while True:
        print(numero)
        numero -=1
        if numero <= 0:
            break


# contagem_regressiva(12)

def contagem_regressiva(numero):
    while True:
        print(numero)
        numero -=1
        if numero <= 0:
            break

# contagem_regressiva(8)

def media(nota1,nota2,nota3):
    media_notas = (nota1+nota2+nota3)/3
    if media_notas >= 7:
        print(f"Aprovado! Média {media_notas}")
    elif media_notas >= 5:
        print(f"Recuperação! {media_notas}")
    else:
        print(f"Reprovado! Média {media}")
    return media_notas

mediu = media(10, 6, 5)
print(mediu)


#AUTOMATIZAR ENTRADAS DO USUÁRIO
quantidade = [1,2,3]
for i in range(quantidade):
    int(input("Entre com os dados: "))