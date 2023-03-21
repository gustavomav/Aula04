valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))

if valor1 > valor2:
    print(f'O valor {valor1} é maior que {valor2}')
elif valor1 < valor2:
    print(f'O valor {valor2} é maior que o valor {valor1}')
else:
    print(f'O valor é inválido')