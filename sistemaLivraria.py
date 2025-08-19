DESCONTO_PADRAO = 0.105
livros, vendas = [], []
op = 0

def cadastrar_livro():
    livro = {"autor": input("Autor do livro: "),
             "titulo": input("Titulo do livro: "),
             "preco": float(input("Preço do livro: ")),
             "qts_estoque": int(input("Quantidade em estoque: ")),}
    if isinstance(livro["preco"], float):
        livros.append(livro)
    else:
        print("O valor do livro precisa ser um valor float")

def listar_livros():
    if not livros:
        print("Nenhum livro foi encontrado.")
    else:
        for livro in livros:
            print(f"\nId: {livros.index(livro)}")
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Preço: R${round(livro['preco'], 2)}")
            print(f"Quantidade em estoque: {round(livro['qts_estoque'], 2)}")

def validar_venda(livro, quantidade):
    if quantidade <= livro['qts_estoque']:
        return True
    else:
        return False

def registrar_venda(livro, quantidade):
    livro['qts_estoque'] -= quantidade
    valor_venda = livro['preco'] * quantidade
    if valor_venda >= 100:
        valor_venda *= (1 - DESCONTO_PADRAO)
    venda = {"produto": livro, "quantidade": quantidade, "valor": valor_venda}
    vendas.append(venda)
    print(f"\nVenda registrada com sucesso! Valor final: R${valor_venda:.2f}")

print("-=" * 5)
print("Livraria")
print("-=" * 5)
while op != 4:
    print("\nESCOLHA UMA OPÇÃO")
    print("[ 1 ] - Cadastrar livro")
    print("[ 2 ] - Vender livro")
    print("[ 3 ] - Listar livros")
    print("[ 4 ] - Encerrar processo")
    op = int(input("\nOpção escolhida: "))
    if op == 1:
        cadastrar_livro()
    elif op == 2:
        if not livros:
            print("Não há livros disponíveis para venda.")
        else:
            print("\nLIVROS À VENDA")
            listar_livros()
            op_venda = int(input("\nInforme o livro que deseja vender: "))
            if isinstance(op_venda, int):
                if op_venda+1 > len(livros):
                    qtde_vendas = int(input("Informe o quantidade que deseja vender: "))
                    if validar_venda(livros[op_venda], qtde_vendas):
                        registrar_venda(livros[op_venda], qtde_vendas)
                    else:
                        print("Quantidade de livros inválida")
                else:
                    print("Opção de venda inválida")
            else:
                print("A opção deve ser um valor inteiro")
    elif op == 3:
        listar_livros()
    elif op == 4:
        print("Saindo do programa...")
    else:
        print("\nOPÇÃO INVÁLIDA!")



