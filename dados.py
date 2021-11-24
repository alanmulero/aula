import random
import termcolor
from termcolor import colored
from time import sleep

print(colored('==//==' * 18,'red'))
print('Vamos jogar dados?')
print(colored('Estou pensando em um numero...','blue'))
sleep(3)
print(colored('Escolha um numero de 1 até o 6.','yellow'))
print(colored('==//==' * 18,'red'))
num = int(input(colored('Digite a sua aposta: ','green')))
dados = (random.randint(1,6))

if dados == num:
    print(f'Vocẽ acertou, o numero que escolhi foi : {dados} ')
elif dados != num:
    print('Gostaria de fazer a sua segunda tentativa?')
    num2 = int(input('Digite a sua segunda aposta: '))
    if dados == num2 :
        print(f'Você acertou, o numero que escolhi foi : {dados} ')
    elif dados != num2:
        print('Gostaria de fazer a sua terceira tentativa?')
        num3 = int(input('Digite a sua ultima aposta: '))
        if num3 == dados:
            print(f'Você acertou, o numero que escolhi foi : {dados} ')
        else:
            print(f'Infelizmente você não acertou, o numero que escolhi foi : {dados} ')
            if dados ==    num + num2:
                print('Você atingiu o maximo de tentativas possiveis.')
else:
    print('Obrigado')












