numero_conta = int(input('Digite o numero da conta: '))
saldo = float(input('Digite seu saldo: '))
debito = float(input('Digite seu débito: '))
credito = float(input('Digite seu crédito: '))

saldo_atual = (saldo -debito) + credito

if saldo_atual > 0:
    print(f'Saldo Positivo de {saldo_atual}')
else:
    print('Saldo Negativo')

