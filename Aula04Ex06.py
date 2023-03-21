qtd_atual = int(input('Digite a quantidade atual no estoque: '))
qtd_max = int(input('Digite a quantidade máxima no estoque: '))
qtd_min = int(input('Digite a quantidade mínima no estoque: '))

qtd_media = (qtd_max + qtd_min) /2

if qtd_atual >= qtd_media:
    print('Não efetuar compra')
else:
    print('efetuar a compra')