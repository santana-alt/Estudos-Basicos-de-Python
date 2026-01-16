#Faça um programa que receberá nomes de pessoas, um por linha, até que o usuário digite "fim". Ao final, agrupe e imprima os nomes de acordo com a primeira letra do nome, ignorando se está em maiúsculo ou minúsculo. Os nomes devem ser agrupados em ordem alfabética da letra inicial e exibidos na ordem de inserção.

nome = str(input())
dicionario = {

}
while nome != "fim":
    if nome[0].upper() in dicionario:
        dicionario[nome[0].upper()] += " " + nome
    else:
        dicionario[nome[0].upper()] = nome
    nome = str(input())
dicionario_ordenado = sorted(dicionario.items())
for letra,nomes in dicionario_ordenado:
    print(f"{letra}: {nomes}")