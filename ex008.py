totAluno = int(input("Informe quantos alunos há na turma: "))
maior = 0
menor = 0
for i in range(0, totAluno):
    nota = float(input(f"Informe a nota do {i+1}° aluno: "))
    #define o maior se não for edfinido anteriormente
    if i == 0:
        maior, menor = nota

    #Calcula maior e menor
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
