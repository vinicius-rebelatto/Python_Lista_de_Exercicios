tot = 0
for i in range (0, 3):
    prod = input(f"Nome do {i+1}° produto: ")
    valor = float(input(f"Falor de {prod}: R$"))
    tot += valor
if tot >= 100:
    print(f"valor de {round(tot, 2)} com desconto de 10% é {round(tot-tot/10, 2)}")
else:
    print(f'valor total: R${round(tot, 2)}')