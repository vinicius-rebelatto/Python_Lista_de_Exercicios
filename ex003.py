number1 = int(input("Informe um número: "))
number2 = int(input("Informe outro número: "))
print(f'{number1} + {number2} = {number1 + number2}')
print(f'{number1} - {number2} = {number1 - number2}')
print(f'{number1} * {number2} = {number1 * number2}')
if number2 != 0:
    print(f'{number1} / {number2} = {number1 / number2}')
else:
    print("Não é possível dividir um número por '0'")