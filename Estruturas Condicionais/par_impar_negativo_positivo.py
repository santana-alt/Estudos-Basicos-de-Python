#Faça um programa para ler quatro números inteiros (n1, n2, n3 e n4) e depois exibir todos que são pares e positivos, pares e negativos, ímpares e positivos, ímpares e negativo e zero, nesta ordem


n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

print("Números pares e positivos:")
if n1 % 2 == 0 and n1 > 0:
    print(n1)
if n2 % 2 == 0 and n2 > 0:
    print(n2)
if n3 % 2 == 0 and n3 > 0:
    print(n3)
if n4 % 2 == 0 and n4 > 0:
    print(n4)

print("\nNúmeros pares e negativos:")
if n1 % 2 == 0 and n1 < 0:
    print(n1)
if n2 % 2 == 0 and n2 < 0:
    print(n2)
if n3 % 2 == 0 and n3 < 0:
    print(n3)
if n4 % 2 == 0 and n4 < 0:
    print(n4)

print("\nNúmeros ímpares e positivos:")
if n1 % 2 != 0 and n1 > 0:
    print(n1)
if n2 % 2 != 0 and n2 > 0:
    print(n2)
if n3 % 2 != 0 and n3 > 0:
    print(n3)
if n4 % 2 != 0 and n4 > 0:
    print(n4)

print("\nNúmeros ímpares e negativos:")
if n1 % 2 != 0 and n1 < 0:
    print(n1)
if n2 % 2 != 0 and n2 < 0:
    print(n2)
if n3 % 2 != 0 and n3 < 0:
    print(n3)
if n4 % 2 != 0 and n4 < 0:
    print(n4)

print("\nNúmeros zeros:")
if n1 == 0:
    print(n1)
if n2 == 0:
    print(n2)
if n3 == 0:
    print(n3)
if n4 == 0:
    print(n4)
