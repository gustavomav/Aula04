nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media > 6:
    print(f'Aluno aprovado, parabéns, sua média foi {media}')
elif media < 6:
    print(f'Aluno reprovado, estude mais, sua média foi {media}')
else:
    print(f'Aluno aprovado, parabéns, sua média foi {media}')