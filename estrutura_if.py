# Exercicio if else.
print(' 1 = Sim')
print(' 2 = Não')
print('3 = Vou pensar sobre.')
corte = int(input('Voce vai cortar o cabelo? '))
if corte == 1:
    escova = int(input('Gostaria de fazer escova também?'))
    if escova == 1:
        print('O valor total é de R$ 90.00')
    else:
        print('Então o valor somente do corte é de R$ 60.00')
mechas = int(input('Voce gostaria de fazer mechas?'))
if mechas == 1:
    hidratar = int(input('Gostaria de hidratar junto com as mechas?'))
    if hidratar == 1:
        print('Então o valor total é de R$ 300,00')
    else:
        print('Somente as méchas fica em R$ 250,00')
tintura = int(input('Voce vai fazer tintura? '))
if tintura == 1:
    vermelho = int(input('Vai usar tons vermelhos? '))
    if vermelho == 1:
        duvida = int(input('Gostaria de tentar uma cor no tom castanho ? '))
        if  duvida == 1:
            print('Realmente o castanho fica melhor em voce!')
        else:
            print('A escolha é sua!')

else:
    print('Obrigado pela paciencia.')









