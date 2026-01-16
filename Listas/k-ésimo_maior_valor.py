#Dada uma lista de números inteiros distintos, escreva um programa que encontre o n-ésimo maior valor da lista.
#O programa deve primeiro ler um inteiro t (tamanho da lista), depois t inteiros distintos n, e por fim um inteiro k, representando a posição do valor desejado na ordem crescente.
#A saída deverá ser o k-ésimo maior valor que está na lista. Obs.: k sempre estará no intervalo do tamanho da lista.

t = int(input())
lista = []

for i in range(t):
    n = int(input())
    lista.append(n)

k = int(input())
lista.sort()
print(lista[k])