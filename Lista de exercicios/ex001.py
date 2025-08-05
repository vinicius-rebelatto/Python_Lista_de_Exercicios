nome = input("Nome do aluno: ")
nota1 = int(input("primeira nota: "))
nota2 = int(input("segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 6:
    print(f'O aluno com média {media} está aprovado')
else:
    print(f'O aluno com média {media} está reprovado')