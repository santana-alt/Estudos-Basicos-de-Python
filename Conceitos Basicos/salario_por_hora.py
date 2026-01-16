#Escreva um programa que leia o salário de uma pessoa, quantas horas ela trabalha por dia e quantos dias ela trabalhou no mês. Em seguida, calcule e exiba quanto essa pessoa recebe por hora.

salario = float(input(""))
horas_por_dia = int(input(""))
dias_trabalhados = int(input(""))

valor_hora = salario / (horas_por_dia * dias_trabalhados)

print(f"Eu recebo uma mixuruca de R$ {valor_hora:.1f} por hora trabalhada.")