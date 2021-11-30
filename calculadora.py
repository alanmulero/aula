# Exercicio laços repetição usando while.
while True:
    print()
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite um operador básico: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Digite um número válido.')
        continue
    num1 = int(num1)
    num2 = int(num2)

    #Definindo operadores:
    if operador == '+' :
        print(num1 + num2)
    elif operador == '-' :
        print(num1 - num2)
    elif operador == '*' :
        print(num1 * num2)
    elif operador == '/' :
        print(num1 / num2)
    else:
        print('Digite um operador válido.')




