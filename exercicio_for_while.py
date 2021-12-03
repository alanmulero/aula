# Exercicio for e while
import termcolor
from termcolor import colored
coluna = 1
linha = 1
print('{:>4}'.format(' '), end=' ')
for coluna in range(1, 11):
    print(f'{coluna:>4}', end=' ')
print()

for coluna in range(1, 11):
    print(colored(f'{coluna:>4}', 'red'),end=' ')
    while linha <= 10:
        print(colored(f'{coluna*linha:>4}', 'blue'),end=' ')
        linha = linha + 1
    print()
    linha = 1

