#Dada uma lista de n números inteiros e um valor inteiro k, crie uma nova lista com os elementos multiplicados por k e imprima o resultado.
#A saída deverá ser os elementos da nova lista, multiplicados por k, na mesma linha, separados por um espaço em branco entre eles.

elementos = list(map(int,input().split()))
k = int(input())
lista = [x*k for x in elementos]
print(*lista,"")