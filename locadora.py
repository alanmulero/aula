try:
     dias = float(input('Quantos dias de aluguel? : '))
     km = float(input('Qual a kilometragem rodada? : '))
except ValueError:
    print('Digite um numero valido')
    breack
else:    
    print(f'O valor do aluguel por dia alugado é de : R${60.00 * dias}')
    print(f'O valor pago pela kilometragem rodada é de : R${km * 0.15}')
    total = (60.00 * dias) + (0.15 * km)
    print(f'O valor total é de : {total:.2f}')
