import json
import os.path

from main import Biblioteca
from livro import Livro
from usuario import Usuario

def exibir_menu():
    print("\nSistema de Biblioteca")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Usuário")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Consultar Livros")
    print("6. Gerar Relatório")
    print("7. Deletar Livro")
    print("8. Deletar Usuário")
    print("9. Salvar Dados")
    print("10. Carregar Dados")
    print("0. Sair")

def main():
    biblioteca = Biblioteca()
    arquivo_dados = "biblioteca_dados.json"

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = int(input("Ano do livro: "))
            num_copias = int(input("Número de cópias: "))
            livro = Livro(titulo=titulo, autor=autor, ano=ano, num_copias=num_copias)
            biblioteca.cadastrar_livro(livro)
            print("Livro cadastrado com sucesso!")

        elif escolha == "2":
            nome = input("Nome do usuário: ")
            contato = input("Contato do usuário: ")
            usuario = Usuario(nome=nome, contato=contato)
            biblioteca.cadastrar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

        elif escolha == "3":
            id_livro = int(input("ID do livro a ser emprestado: "))
            id_usuario = int(input("ID do usuário: "))
            if biblioteca.emprestar_livro(id_livro, id_usuario):
                print("Empréstimo realizado com sucesso!")
            else:
                print("Erro ao realizar empréstimo. Verifique os IDs ou a disponibilidade.")

        elif escolha == "4":
            id_livro = int(input("ID do livro a ser devolvido: "))
            id_usuario = int(input("ID do usuário: "))
            if biblioteca.devolver_livro(id_livro, id_usuario):
                print("Livro devolvido com sucesso!")
            else:
                print("Erro ao devolver livro. Verifique os IDs.")

        elif escolha == "5":
            parametro = input("Digite o título, autor ou ano do livro: ")
            livros = biblioteca.consultar_livros(parametro)
            if livros:
                print("\nLivros encontrados:")
                for livro in livros:
                    print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Cópias Disponíveis: {livro.num_copias}")
            else:
                print("Nenhum livro encontrado.")

        elif escolha == "6":
            print("\nRelatório:")
            print(biblioteca.gerar_relatorio())

        elif escolha == "7":
            id_livro = int(input("ID do livro a ser deletado: "))
            if biblioteca.deletar_livro(id_livro):
                print("Livro deletado com sucesso!")
            else:
                print("Erro ao deletar livro. Ele pode estar emprestado.")

        elif escolha == "8":
            id_usuario = int(input("ID do usuário a ser deletado: "))
            if biblioteca.deletar_usuario(id_usuario):
                print("Usuário deletado com sucesso!")
            else:
                print("Erro ao deletar usuário. Ele pode ter livros emprestados.")

        elif escolha == "9":
            biblioteca.salvar_dados(arquivo_dados)
            print("Dados salvos com sucesso!")

        elif escolha == "10":
            biblioteca.carregar_dados(arquivo_dados)
            print("Dados carregados com sucesso!")

        elif escolha == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
