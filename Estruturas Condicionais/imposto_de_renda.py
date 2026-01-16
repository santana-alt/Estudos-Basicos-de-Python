#Faça um programa que leia o valor da diária de um funcionário, a quantidade de dias que este trabalhou no mês e exiba o salário bruto, o Imposto de Renda (IR) a ser pago e o salário líquido. O cálculo do IR deve considerar os seguintes percentuais:
#Salário até R$2.000,00 é isento de IR;Salário entre R$2.000,00 e R$5.000,00 deve pagar 15% de IR;Salário superior a R$5.000,00 deve pagar 27,5% de IR.

valor_diaria = float(input())
dias_trabalhados = int(input())

salario_bruto = valor_diaria * dias_trabalhados

if salario_bruto <= 2000:
    print("Você está isento do Imposto de Renda.")
    print(f"Seu salário é: R$ {salario_bruto:.2f}")

elif salario_bruto <= 5000:
    ir = salario_bruto * 0.15
    salario_liquido = salario_bruto - ir
    print("Você não está isento do Imposto de Renda.")
    print(f"Seu salário bruto é de: R$ {salario_bruto:.2f}")
    print(f"Seu valor do IR é: R$ {ir:.2f}")
    print(f"Seu salário líquido é de: R$ {salario_liquido:.2f}")

else:
    ir = salario_bruto * 0.275
    salario_liquido = salario_bruto - ir
    print("Você não está isento do Imposto de Renda.")
    print(f"Seu salário bruto é de: R$ {salario_bruto:.2f}")
    print(f"Seu valor do IR é: R$ {ir:.2f}")
    print(f"Seu salário líquido é de: R$ {salario_liquido:.2f}")
