import random
count = 0
while count <= 3:
    escolha = input('Escolha "p" para par, ou "i" para impar: ')
    escolha = len(escolha)
    if escolha == 'i':
        escolha == 1
    comput = (random.randint(0,3))
    soma = escolha + comput 
    if (soma%2) == 0:
        print('O par ganhou.')
    else:
        print('O impar ganhou')
    print(f'A soma dos apostadores foi: ==> {soma}')
    count +=1
print('Terminou')