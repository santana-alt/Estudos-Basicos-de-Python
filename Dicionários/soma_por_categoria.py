#Faça um programa que receberá n pares de dados: uma categoria e um valor inteiro. O seu código deve somar os valores por categoria e imprimir o total de cada uma.

n = int(input(""))
dicionario = {

    }
for x in range(n):
    partes_dicionario = input("").split()
    categoria = str(partes_dicionario[0])
    valor = int(partes_dicionario[1])

    if categoria in dicionario:
        dicionario[categoria] += valor
    else:
        dicionario[categoria] = valor

for categoria,valor_total in dicionario.items():
    print(f"{categoria}: {valor_total}")