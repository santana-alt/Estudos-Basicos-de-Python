#Crie uma função alunos_acima_da_media(nomes, notas) que recebe duas listas com os nomes e as notas dos alunos. Após isso, o programa deverá ser capaz de exibir o nome dos alunos que foram aprovados (nota >= 7)

def alunos_acima_da_media(nomes, notas):
    for nomes,notas in zip(nomes,notas):
        if notas>=7:
            print(nomes)

n = int(input())
nomes = []
notas = []
for x in range(n):
    nomes_do_aluno = str(input(""))
    nota_do_aluno = float(input(""))
    nomes.append(nomes_do_aluno)
    notas.append(nota_do_aluno)
print(f"Os alunos que foram aprovados foram: ")
alunos_acima_da_media(nomes,notas)
