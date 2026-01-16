#Dado um número inteiro positivo n, crie um dicionário onde as chaves vão de 1 até n, e os valores são os quadrados das chaves.

n = int(input())
for x in range(1, n+1):
    valor = x **2
    chave = x
    dicionario = {
        chave:valor
    }
    for a,b in dicionario.items():
        print(f"{chave}: {valor}")