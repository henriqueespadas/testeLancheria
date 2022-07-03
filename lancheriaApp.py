def lancheria() -> None:
    print('Olá, Seja bem vindo')

    produtos = [
        {'nome': 'Cachoro quente', 'codigo': 100, 'preco': 1.20, 'quantidade': 0},
        {'nome': 'Bauru simples', 'codigo': 101, 'preco': 1.30, 'quantidade': 0},
        {'nome': 'Bauro com ovo', 'codigo': 102, 'preco': 1.50,'quantidade': 0},
        {'nome': 'Hamburger', 'codigo': 103, 'preco': 1.20,'quantidade': 0},
        {'nome': 'Chesseburguer', 'codigo': 104, 'preco': 1.30,'quantidade': 0},
        {'nome': 'Refrigerante', 'codigo': 105, 'preco': 1.00,'quantidade': 0},
    ]

    def adicionar_produto(nome: str, codigo: int, preco: float) -> None:
        """
            Função para adicionar um novo produto no dict produtos.
        :param nome:
        :param codigo:
        :param preco:
        :return: none
        """
        produtos.append({'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': 0})
        print("Dados cadastrados")

    def listar_cardapio() -> None:
        """
            Função para listar o cardápio.
        """
        print('O cardápio é o seguinte:')
        for produto in produtos:
            print(f"{produto['nome']} -> preço {produto['preco']}$ - código: {produto['codigo']}")

    listar_cardapio()
    preco_total = 0

    while True:
        acao = input('Se deseja adicionar um produto, digite 1, se deseja finalizar a compra, digite 2, e para ver o cardápio novamente, digite 3: ')

        if acao == '1':
            codigo = int(input('Digite o código do produto desejado: '))
            quantidade = int(input('Digite a quantidade de itens do produto desejado: '))
            for produto in produtos:
                if produto['codigo'] == codigo:
                    preco_total += produto['preco'] * quantidade
                    produto['quantidade'] += quantidade
                    print(produto['quantidade'])
                    continue

        elif acao == '2':
            print(round(preco_total, 2))
            for produto in produtos:
                if produto['quantidade'] != 0:
                    print(f"Foram vendidos {produto['quantidade']}{produto['nome']}, com um total de {round(produto['quantidade'] * produto['preco'], 2)}$")
            print(f"O valor total foi de {round(preco_total, 2)}$")
            break

        elif acao == '3':
            listar_cardapio()

        elif acao == '999':
            nome_produto = input('Digite o nome do produto')
            codigo_produto = int(input('Digite o código do produto'))
            preco_produto = float(input('Digite o preço do produto'))
            adicionar_produto(nome_produto, codigo_produto, preco_produto)

        else:
            print("Número inválido, digite novamente")
            continue

lancheria()