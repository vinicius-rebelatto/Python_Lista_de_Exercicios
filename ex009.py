frase = input("Informe uma palavra ou frase para verificar se é palíndomo: ")
if frase.replace(' ', '')[::-1].lower() == frase.replace(' ', '').lower():
    print(f'É palindromo')
else:
    print('Não é palindromo')