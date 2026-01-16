#Faça um programa que armazena números de telefone de algumas pessoas em um dicionário. O programa deve receber entradas no formato nome telefone, uma por linha, até que o usuário digite "fim" para encerrar o cadastro. Depois disso, o programa deve ler um nome e imprimir o número correspondente, caso exista no dicionário.
#Atenção: a variável nome pode ser tanto maiuscula quanto minuscula e mesmo assim deve exibir o número correspondente, caso exista.

linha = str(input("")).split()
telefonica = {

}
while linha[0] != "fim":
    nome = linha[0].lower()
    telefone = linha[1].lower()
    telefonica[nome] = telefone
    linha = str(input("")).split()
consulta = str(input("")).lower()
if consulta in telefonica:
    print(telefonica.get(consulta))
else:
    print("Essa pessoa não está na lista telefônica")