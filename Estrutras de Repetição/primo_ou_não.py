#Escreva um programa que recebe um número inteiro n e imprime Sim se ele for um número primo, ou Não caso contrário.

n = int(input(""))

if n % 2 != 0:
    print("Sim, esse número é primo")
else:
    print("O número não é primo")