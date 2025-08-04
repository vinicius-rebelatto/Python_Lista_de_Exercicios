idade = int(input("Informe uma idade: "))
if idade <= 12:
    print("É Criança")
elif idade <= 17:
    print("É Adolescente")
elif idade <= 59:
    print("É Adulto")
else:
    print("É Idoso")