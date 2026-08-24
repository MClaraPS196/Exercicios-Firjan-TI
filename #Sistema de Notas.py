#Sistema de Notas
#Uma escola deseja um sistema para calcular a situação dos alunos. Para cada aluno, o professo informa três notas.
#O sistema deve calcular a média e informar: Aprovado: média >= 7; Recuperação: m[´pedoa >= 5 e 7; Reprovado: média < 5. 
# O professor deverá cadastrar vários alunos, e ao final, o sistema deverá informar a quantidade de aprovados, em recuperação e reprovados.
#Responda: Quantas notas precisam ser armazenadas por aluno? Qual cálculo deve ser realizado? Quais contadores são necessários? Quando o cadastro deve terminar?

# RF001 -> O sistema deve possibilitar calcular a média das notas
# Regras de Negócio: media>=7: Aprovado, Media>7 e >=5: Recuperação, Media < 5: Reprovado

# VARIÁVEIS GLOBAIS
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 =  float(input("Digite a segunda nota: "))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print(f"Aluno Aprovado! Média {media}")
elif media >= 5:
    print(f"Aluno em Recuperação! Média {media}")
else:
    print(f"Aluno Reprovado! Média {media}")


def media(nota1,nota2,nota3):
    media_notas = (nota1+nota2+nota3)/3 #VARIÁVEL LOCAL
    if media_notas >= 7:
        print(f"Aprovado! Média {media_notas}")
    elif media_notas >= 5:
        print(f"Recuperação! {media_notas}")
    else:
        print(f"Reprovado! Média {media}")

media(nota1, nota2, nota3)

#REVISA CÓDIGO
def informa_notas():
    notas1 = float(input("Digite a primeira nota!: "))
    notas2 = float(input("Digite a segunda nota!: "))
    notas3 = float(input("Digite a terceira nota!: "))

    media(notas1, notas2, notas3)

informa_notas()

def sistema_notas():

    quantidade_notas = int(input("Entre com a quantidade de notas: "))
    for i in range(quantidade_notas):

        notas_total = float(input("Entre com as notas: "))

        media_total = media()
        status = media()
        print(status)

sistema_notas()
