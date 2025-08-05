num = int(input("Informe um número: "))
interval = int(input("Informe até que numero quer a tabuada: "))
for i in range(1, interval+1):
    print(f'{num} x {i} = {num*i}')