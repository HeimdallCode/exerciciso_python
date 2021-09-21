# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 23 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que mostre todos os primos entre 1 e N sendo N um número
# inteiro fornecido pelo usuário. O programa deverá mostrar também o número
# de divisões que ele executou para encontrar os números primos. Serão
# avaliados o funcionamento, o estilo e o número de testes (divisões) executados.


n = int(input('\nDigite um numero: '))
k = 0 

for j in range(n):
    for i in range(2,n):
        if n%i == 0:
            print(f'{n} divisivel por {i}')
            k +=1

    if k == 0:
        print(f'\033[1;32m{n} é primo\033[1;m\n')
    else:
        print(f'\033[1;31m{n} não é primo\033[1;m\n')