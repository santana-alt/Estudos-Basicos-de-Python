#Faça um programa que leia o nome e a nota de vários alunos (a entrada termina quando for digitado um nome vazio OU quando a entrada for "fim"). Armazene os nomes em uma lista e as notas em outra. Em seguida, exiba os nomes dos alunos ordenados da maior para a menor nota.
#O programa deverá exibir nome e nota, da maior para a menor nota, separado linha a linha.
#Obs.: caso as notas sejam as mesmas, exibir por ordem de entrada no programa.
#Obs.: a saída de notas deve ter 2 casas decimais

lista_alunos = []
lista_notas = []

nome_aluno = str(input())


while nome_aluno != "fim":
    lista_alunos.append(nome_aluno)
    nota_aluno = float(input(""))
    lista_notas.append(nota_aluno)
    nome_aluno = input()
    if nome_aluno == "fim" or nome_aluno == "":
        break
lista_ordenada = sorted(zip(lista_notas,lista_alunos), reverse=True)

for nota,nome in lista_ordenada:
    print(f"{nome}: {nota:.2f}")