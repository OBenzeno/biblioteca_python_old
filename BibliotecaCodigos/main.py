import PySimpleGUI as sg
from livro import Livro
from usuario import Usuario
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    # Carregar dados se o arquivo existir
    filename = 'biblioteca_dados.json'
    biblioteca.carregar_dados(filename)

    layout = [
        [sg.Button('Cadastrar Livro'), sg.Button('Cadastrar Usuário')],
        [sg.Button('Empréstimo de Livro'), sg.Button('Devolução de Livro')],
        [sg.Button('Consulta de Livros'), sg.Button('Gerar Relatório')],
        [sg.Button('Deletar Livro'), sg.Button('Deletar Usuário')],
        [sg.Output(size=(50, 20))],
        [sg.Button('Sair')]
    ]

    window = sg.Window('Sistema de Gerenciamento de Biblioteca', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break

        if event == 'Cadastrar Livro':
            layout_cadastro_livro = [
                [sg.Text('Título'), sg.InputText(key='-TITULO-')],
                [sg.Text('Autor'), sg.InputText(key='-AUTOR-')],
                [sg.Text('Ano'), sg.InputText(key='-ANO-', enable_events=True)],
                [sg.Text('Número de Cópias'), sg.InputText(key='-COPIAS-', enable_events=True)],
                [sg.Button('Cadastrar')]
            ]
            window_cadastro_livro = sg.Window('Cadastrar Livro', layout_cadastro_livro)
            while True: #Loop para aceitar somente números para o ano e o número de cópias.
                event, values = window_cadastro_livro.read()
                if event == sg.WINDOW_CLOSED:
                    break
                if event == 'Cadastrar':
                    try:
                        ano = int(values['-ANO-'])
                        num_copias = int(values['-COPIAS-'])
                        livro = Livro(values['-TITULO-'], values['-AUTOR-'], ano, num_copias)
                        biblioteca.cadastrar_livro(livro)
                        print("Livro cadastrado com sucesso!")
                        break
                    except ValueError:
                        sg.popup_error('Por favor, insira um número válido para o ano e o número de cópias.')
            window_cadastro_livro.close()

        if event == 'Cadastrar Usuário':
            layout_cadastro_usuario = [
                [sg.Text('Nome'), sg.InputText(key='-NOME-')],
                [sg.Text('Contato'), sg.InputText(key='-CONTATO-', enable_events=True)],
                [sg.Button('Cadastrar')]
            ]
            window_cadastro_usuario = sg.Window('Cadastrar Usuário', layout_cadastro_usuario)
            while True: #Loop para aceitar somente números para o contato. 
                event, values = window_cadastro_usuario.read()
                if event == sg.WINDOW_CLOSED:
                    break
                if event == 'Cadastrar':
                    contato = values['-CONTATO-']
                    if not contato.isdigit():
                        sg.popup_error('Por favor, insira apenas números para o contato.')
                        continue
                    usuario = Usuario(values['-NOME-'], contato)
                    biblioteca.cadastrar_usuario(usuario)
                    print("Usuário cadastrado com sucesso!")
                    break
            window_cadastro_usuario.close()

        if event == 'Empréstimo de Livro':
            layout_emprestimo = [
                [sg.Text('ID do Livro'), sg.InputText(key='-ID_LIVRO-', enable_events=True)],
                [sg.Text('ID do Usuário'), sg.InputText(key='-ID_USUARIO-', enable_events=True)],
                [sg.Button('Emprestar')]
            ]
            window_emprestimo = sg.Window('Empréstimo de Livro', layout_emprestimo)
            while True: #Loop para aceitar somente números para o ID do livro e do usuário. 
                event, values = window_emprestimo.read()
                if event == sg.WINDOW_CLOSED:
                    break
                if event == 'Emprestar':
                    try:
                        id_livro = int(values['-ID_LIVRO-'])
                        id_usuario = int(values['-ID_USUARIO-'])
                        if biblioteca.emprestar_livro(id_livro, id_usuario):
                            print("Livro emprestado com sucesso!")
                        else:
                            print("Não foi possível emprestar o livro.")
                    except ValueError:
                        sg.popup_error('Por favor, insira um número válido para o ID do livro e do usuário.')
                    break
            window_emprestimo.close()

        if event == 'Devolução de Livro':
            layout_devolucao = [
                [sg.Text('ID do Livro'), sg.InputText(key='-ID_LIVRO-', enable_events=True)],
                [sg.Text('ID do Usuário'), sg.InputText(key='-ID_USUARIO-', enable_events=True)],
                [sg.Button('Devolver')]
            ]
            window_devolucao = sg.Window('Devolução de Livro', layout_devolucao)
            while True: #Loop para aceitar somente números para o ID do livro e do usuário. 
                event, values = window_devolucao.read()
                if event == sg.WINDOW_CLOSED:
                    break
                if event == 'Devolver':
                    try:
                        id_livro = int(values['-ID_LIVRO-'])
                        id_usuario = int(values['-ID_USUARIO-'])
                        if biblioteca.devolver_livro(id_livro, id_usuario):
                            print("Livro devolvido com sucesso!")
                        else:
                            print("Não foi possível devolver o livro.")
                    except ValueError:
                        sg.popup_error('Por favor, insira um número válido para o ID do livro e do usuário.')
                    break
            window_devolucao.close()

        if event == 'Consulta de Livros':
            layout_consulta = [
                [sg.Text('Título, Autor ou Ano de Publicação'), sg.InputText(key='-PARAMETRO-')],
                [sg.Button('Consultar')]
            ]
            window_consulta = sg.Window('Consulta de Livros', layout_consulta)
            while True:
                event, values = window_consulta.read()
                if event == sg.WINDOW_CLOSED:
                    break
                if event == 'Consultar':
                    livros_encontrados = biblioteca.consultar_livros(values['-PARAMETRO-'])
                    if livros_encontrados:
                        print("Livros encontrados:")
                        for livro in livros_encontrados:
                            print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Cópias Disponíveis: {livro.num_copias}")
                    else:
                        print("Nenhum livro encontrado com esse parâmetro.")
                    break
            window_consulta.close()

        if event == 'Gerar Relatório':
            print(biblioteca.gerar_relatorio())

        if event == 'Deletar Livro':
            layout_deletar_livro = [
                [sg.Text('ID do Livro a ser deletado:'), sg.InputText(key='-ID_LIVRO-', enable_events=True)],
                [sg.Button('Deletar')]
            ]
            window_deletar_livro = sg.Window('Deletar Livro', layout_deletar_livro)
            while True: #Loop para aceitar somente números para o ID do livro. 
                event, values = window_deletar_livro.read()
                if event == sg.WINDOW_CLOSED:
                    break
                if event == 'Deletar':
                    try:
                        id_livro = int(values['-ID_LIVRO-'])
                        if biblioteca.deletar_livro(id_livro):
                            print("Livro deletado com sucesso!")
                        else:
                            print("Livro não encontrado ou já foi emprestado.")
                    except ValueError:
                        sg.popup_error('Por favor, insira um número válido para o ID do livro.')
                    break
            window_deletar_livro.close()

        if event == 'Deletar Usuário':
            layout_deletar_usuario = [
                [sg.Text('ID do Usuário a ser deletado:'), sg.InputText(key='-ID_USUARIO-', enable_events=True)],
                [sg.Button('Deletar')]
            ]
            window_deletar_usuario = sg.Window('Deletar Usuário', layout_deletar_usuario)
            while True: #Loop para aceitar somente números para o ID do usuário. 
                event, values = window_deletar_usuario.read()
                if event == sg.WINDOW_CLOSED:
                    break
                if event == 'Deletar':
                    try:
                        id_usuario = int(values['-ID_USUARIO-'])
                        if biblioteca.deletar_usuario(id_usuario):
                            print("Usuário deletado com sucesso!")
                        else:
                            print("Usuário não encontrado ou possui empréstimos pendentes.")
                    except ValueError:
                        sg.popup_error('Por favor, insira um número válido para o ID do usuário.')
                    break
            window_deletar_usuario.close()

    # Salvar dados antes de sair
    biblioteca.salvar_dados(filename)
    window.close()

if __name__ == "__main__":
    main()

