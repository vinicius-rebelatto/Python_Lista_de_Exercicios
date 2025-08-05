nota = float(input(f"Informe a nota do aluno: "))
frequencia = float(input(f"Informe a frequencia do aluno: "))
if nota >= 6 and frequencia >= 75:
    print('APROVADO')
else:
    print('REPROVADO')