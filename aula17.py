#  Exercicio de fixação em python.
#  Verificar so o numero é par ou impar.
num = input('Digite um numero: ')

if num.isdigit():
    num = int(num)

    if num % 2 == 0:
        print(f'O {num} é um numero par.')
    else:
        print(f'O {num} é um numero impar.')

else:
    print('Voce não digitou um numero inteiro.')




       

#  Exercicio para verificar a hora digitada pelo usuario e retornar, bom dia, boa tarde ou boa noite.
import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)


hora = input('Digite que horas são: ')    
if is_number(hora):
    hora = float(hora)
else:
    print('Por favor, use apenas o "." para informar as horas.\n Exemplo 5.30')    

if hora >= 0.00 and  hora < 11.59 :
    print('Boa dia.')
elif hora >=12.00 and  hora < 18.00:
    print('Boa tarde') 
else:
    print('Boa noite.')       
#  Exercicio contando o numero de caracteres do nome digitado.
nome = input('Digite o seu nome: ')
qtd_caracteres = len(nome)
if qtd_caracteres <= 4:
    print(f' o nome {nome} tem a quantidade de,{qtd_caracteres} caracteres e é um nome pequeno.')
elif qtd_caracteres > 4 and qtd_caracteres <= 6:
    print(f' o nome {nome} tem a quantidade de,{qtd_caracteres} caracteres e é um nome médio.')
else:
        print(f' o nome {nome} tem a quantidade de,{qtd_caracteres} caracteres e é um nome grande.')
