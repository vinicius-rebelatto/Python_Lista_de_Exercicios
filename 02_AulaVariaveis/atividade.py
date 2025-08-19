#peça nome do produto e preço unitario
#peça a quantidade e calcule o valor final
#use pelo menos uma constante para definir um desconto de 10%
#exiba o valor bruto, o desconto e o valor com desconto 
Desconto = 10
nome = input("Nome do produto: ")
valor = float(input("Valor do produto: R$"))
quantidade = int(input("Quantos itens desse produto você quer comprar? "))
print(f"O valor total é R${valor*quantidade}")
print(f"O valor com um desconto de {Desconto}% é R${round(valor*quantidade-((valor*quantidade))/10,2)}")