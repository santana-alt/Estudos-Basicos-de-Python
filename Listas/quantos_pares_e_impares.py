#Escreva um programa em Python que permita ao usuário digitar uma quantidade indeterminada de números inteiros, um por vez. Depois, o programa deverá exibir a quantidade de números digitados, a quantidade de números pares e a quantidade de números ímpares.
#A variável de confirmacao só coletará um novo número SE o usuário digitar 's' ou 'S', indicando que ele quer digitar um novo valor.

numero = int(input())
confirmacao = str(input())
soma_pares = 0
soma_impares = 0
qtd_total = []
qtd_total.append(numero)

while confirmacao == "s":
    numero = int(input())
    qtd_total.append(numero)
    confirmacao = str(input())
for i in qtd_total:
    if i % 2 == 0:
        soma_pares += i
    elif i % 2 != 0:
        soma_impares += i
print(f"Quantidade de números digitados: {len(qtd_total)}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
