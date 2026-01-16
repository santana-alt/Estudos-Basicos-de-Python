#Escreva um programa que receba o nome de uma pessoa e sua idade em anos. O programa deve calcular e exibir a idade da pessoa em meses e dias. Obs.: Considere que um ano tem 12 meses e 365 dias.

nome = str(input(""))
idade_anos = int(input(""))

idade_meses = idade_anos * 12
idade_dias = idade_anos * 365

print(f"{nome} tem {idade_anos} anos ou {idade_meses} meses ou ainda {idade_dias} dias!")