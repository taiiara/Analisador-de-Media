# Analisador de média Versão 1.0
# Por Taiiara

nota1 = float(input('Quanto você tirou no primeiro bimestre? '))
nota2 = float(input('Quanto você tirou no segundo bimestre? '))
media = (nota1 + nota2) / 2

if media <= 5:
    print(f'Sua média final é {media:.1f} e você está reprovado(a)!')
    print(f'Estude mais da próxima vez!')
elif 5.1 <= media <= 6.9:
    print(f'Sua média final é {media:.1f} e você está de recuperação!')
    print('Boa sorte na prova!')
else:
    print(f'Sua média final é {media:.1f} e você está aprovado(a)!')
    print('Parabéns!')
