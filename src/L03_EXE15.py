# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 15 Python Brasil (J.Siqueira 03/21)."""

# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,
# ... Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("\nInforme numero para gerar a sequencia de Fibonacci: "))
j = 0
i = 1

for k in range(n):
    t = i + j
    i = j
    j = t
    print(i, end=", ")
print("\n")
