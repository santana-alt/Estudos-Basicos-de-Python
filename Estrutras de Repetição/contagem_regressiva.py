#Faça um programa que, dado um número, faça a contagem regressiva até 0 para saber a hora do lançamento de um foguete
n = int(input())

for i in range(n, -1, -1):
    print(i)
    if i == 0:
        print("O foguete decolou!")