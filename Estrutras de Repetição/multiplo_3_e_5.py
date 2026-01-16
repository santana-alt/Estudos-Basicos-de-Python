#Faça um programa que, dado um valor n, exiba os valores de 0 a n que são múltiplos de 3, de 5 e de ambos.


n = int(input())

for numero in range(0, n +1):
    if numero % 3 == 0 and numero % 5== 0:
        print(f"{numero} é múltiplo de 3 e de 5")
    elif numero % 3 == 0:
        print(f"{numero} é múltiplo de 3")
    elif numero % 5 == 0:
        print(f"{numero} é múltiplo de 5")