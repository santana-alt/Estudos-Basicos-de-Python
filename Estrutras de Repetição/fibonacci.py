#Faça um programa que, dado um número inteiro n, imprima todos os termos da sequência de Fibonacci menores ou iguais a n, linha a linha.

termo = int(input())

a=0
b = 1

while a <= termo:
    print(a)
    a, b = b, a + b
