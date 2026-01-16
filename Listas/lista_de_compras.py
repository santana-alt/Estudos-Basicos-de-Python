#Escreva um programa em Python que simule uma lista de compras. O usuário deve poder digitar itens livremente, um por vez, e o programa deve armazená-los em uma lista. A entrada termina quando o usuário digitar a palavra "fim" (caso-insensitivo). Ao final, exiba todos os itens da lista em ordem alfabética crescente.
#A saída deverá exibir cada um dos itens da lista de compras, organizados em ordem alfabética crescente, linha a linha.

item = str(input())
lista_compras = []

while item != "fim":
    lista_compras.append(item)
    item = str(input())
lista_compras.sort()
for i in lista_compras:
    print(i)