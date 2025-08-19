produtos = []
for i in range(3):
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    produtos.append({'nome': nome, 'valor': valor})
for produto in produtos:
    print(f"\n{produto['nome']}")
    print(f"R${round(produto['valor'], 2)}")
