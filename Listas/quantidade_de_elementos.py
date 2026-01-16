#Escreva um programa que recebe valores para serem adicionados numa lista. Após isso, o programa deverá exibir quantas vezes os valores aparecem dentro da lista.
#Enquanto confirmacao for "s" ou "S", receber valores para a variável n. Quando confirmacao for diferente do esperado, exibir quantas vezes os elementos aparecem dentro dela.
#Seu programa não deve exibir a mesma mensagem para o número 2 simplesmente porque ele aparece duas vezes na lista.

n = float(input())
confirmacao = str(input()).lower()
lista = []
lista.append(n)
vistos = set()

while confirmacao == "s":
    n = float(input())
    lista.append(n)
    confirmacao = str(input()).lower()

for i in lista:
    if i not in vistos:
        vistos.add(i)
        quantidade_repeticoes = lista.count(i)
        print(f"O elemento {i} aparece {quantidade_repeticoes} vezes na lista")
        