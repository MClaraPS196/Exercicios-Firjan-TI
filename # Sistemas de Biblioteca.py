# Sistemas de Biblioteca
# A ser editado

def main(livros_disponiveis, livros_emprestados):
    livros_disponiveis = 50
    livros_emprestados = 0
    escolha = 10 #10 opções para o usuário escolher, tbm um número diferente de 0 para sempre cair no while abaixo
    return livros_disponiveis, livros_emprestados, escolha

def sistema_biblioteca(escolha):
    
    while escolha != 0:
        print("=====SISTEMA DE BIBLIOTECA=====")
        print("1 - Emprestar Livro")
        print("2 - Devolver Livro")
        print("3 - Consultar Estoque Livros")
        print("0 - Sair")

        escolha = int(input("Digite uma opção para começar: "))

def empresta_livro(livros_disponiveis, livros_emprestados, escolha):
        if escolha == 1:
            if livros_disponiveis > 0:
                livros_disponiveis = livros_disponiveis - 1
                livros_emprestados = livros_emprestados + 1
                print("Empréstimo realizado com sucesso!")
            else:
                print("Não há livros disponíveis na Biblioteca!")
            return  livros_disponiveis, livros_emprestados

        
def consulta_estoque(livros_disponiveis, livros_emprestados, escolha):
        if escolha == 3:
            print(f"Quantidade de Livros Disponíveis na Biblioteca: {livros_disponiveis}")
            print(f"Livros emprestados na Biblioteca: {livros_emprestados}")
        return livros_emprestados, livros_disponiveis

def encerra_sist(livros_disponiveis, livros_emprestados, escolha):
        if escolha == 0:
            print("Sistema finalizado com sucesso!")
        else:
            print("Opção inserida pelo usuário não é válida!")
            print("\n")

        return  livros_disponiveis, livros_emprestados


def devolve_livro(livros_disponiveis, livros_emprestados, escolha):
    if escolha == 2:
        if livros_emprestados > 0:
            livros_emprestados = livros_emprestados - 1
            livros_disponiveis = livros_disponiveis + 1
            print("Livros Devolvidos com Sucesso!")
        else:
            print("Erro! Não há livros emprestados para devolução!")
        return  livros_disponiveis, livros_emprestados
        
            

