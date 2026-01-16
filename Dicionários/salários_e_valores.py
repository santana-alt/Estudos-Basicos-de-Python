#Faça um programa para ler cpf, nome, salário de 10 funcionários. Ao final da leitura, exibir os nomes e salários de quem tem salário abaixo e acima da média, nessa ordem.

funcionarios = []

for x in range(10):
    cpf = str(input(""))
    nome = str(input(""))
    salario = float(input(""))
    
    funcionarios_dicionario = {
        "cpf": cpf,
        "nome": nome,
        "salario": salario
    }
    funcionarios.append(funcionarios_dicionario)
soma = 0
for i in funcionarios:
    soma += i["salario"]
media_salario = soma / 10
acima_media = []
abaixo_media = []

for i in funcionarios:
    if i["salario"] < media_salario:
        abaixo_media.append(i)
    elif i["salario"] > media_salario:
        acima_media.append(i)

print("Abaixo da média:")
for i in abaixo_media:
    print(f"{i['cpf']} {i['nome']}")
print("")
print("Acima da média:")
for i in acima_media:
    print(f"{i['cpf']} {i['nome']}")