#Escreva um programa que, dado um valor n, escreva a tabuada desse número (n x 1 até n x 10)

numero = int(input())
for num in range(1, 11):
        resultado = numero * num
        print(f"{numero} x {num} = {resultado}")