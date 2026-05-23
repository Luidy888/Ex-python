def cadastrar_livro(id): 

    print('-' * 30) 

    print('-----MENU CADASTRAR LIVRO------') 

    nome = input('Por favor entre com o nome do livro: ') 

    autor = input('Por favor entre com o autor do livro: ') 

    editora = input('Por favor entre com a editora do livro: ') 

    livro = { 

        'id': id, 

        'nome': nome, 

        'autor': autor, 

        'editora': editora 

    } 

    lista_livro.append(livro) 

 

def consultar_livro(): 

    while True: 

        print('-' * 30) 

        print("-----MENU CONSULTAR LIVRO-----") 

        print('Escolha a opção desejada:') 

        print('1 - Consultar Todos os Livros') 

        print('2 - Consultar Livro por id') 

        print('3 - Consultar Livro(s) por autor') 

        print('4 - Retornar') 

        opcao = input('>> ') 

         

        if opcao == '1': 

            for livro in lista_livro: 

                print('-' * 30) 

                print(f'id: {livro["id"]}') 

                print(f'nome: {livro["nome"]}') 

                print(f'autor: {livro["autor"]}') 

                print(f'editora: {livro["editora"]}') 

        elif opcao == '2': 

            id_consulta = int(input('Digite o id do livro: ')) 

            encontrado = False 

            for livro in lista_livro: 

                if livro['id'] == id_consulta: 

                    print('-' * 30) 

                    print(f'nome: {livro["nome"]}') 

                    print(f'autor: {livro["autor"]}') 

                    print(f'editora: {livro["editora"]}') 

                    encontrado = True 

            if not encontrado: 

                print('Id inválido') 

        elif opcao == '3': 

            autor_consulta = input('Digite o autor do(s) livro(s): ') 

            encontrado = False 

            for livro in lista_livro: 

                if livro['autor'].lower() == autor_consulta.lower(): 

                    print('-' * 30) 

                    print(f'id: {livro["id"]}') 

                    print(f'nome: {livro["nome"]}') 

                    print(f'autor: {livro["autor"]}') 

                    print(f'editora: {livro["editora"]}') 

                    encontrado = True 

            if not encontrado: 

                print('Autor não encontrado') 

        elif opcao == '4': 

            break 

        else: 

            print('Opção inválida') 

 

def remover_livro(): 

    print('-' * 30) 

    print('------MENU REMOVER LIVRO---------') 

    id_remover = int(input('Digite o id do livro a ser removido: ')) 

    for livro in lista_livro: 

        if livro['id'] == id_remover: 

            lista_livro.remove(livro) 

            print('Livro removido com sucesso!') 

            return 

    print('Id inválido') 

 

print('Bem Vindo a Livraria do Luidy Oliveira') 

lista_livro = [] 

id_global = 0 

 

while True: 

    print('-' * 30) 

    print('--------MENU PRINCIPAL--------') 

    print('Escolha a opção desejada:') 

    print('1 - Cadastrar Livro') 

    print('2 - Consultar Livro(s)') 

    print('3 - Remover Livro') 

    print('4 - Sair') 

    opcao = input('>> ') 

 

    if opcao == '1': 

        id_global += 1 

        cadastrar_livro(id_global) 

    elif opcao == '2': 

        consultar_livro() 

    elif opcao == '3': 

        remover_livro() 

    elif opcao == '4': 

        print('Programa encerrado.') 

        break 

    else: 

        print('Opção inválida') 