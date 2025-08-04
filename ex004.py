peso = float(input("Informe o peso do usuário (Kg): "))
altura = float(input("Informe a altura do usuário (m): "))
imc = round(peso / (altura * altura), 2)
print(f'O IMC do usuário é {imc}')