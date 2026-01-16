#Faça um programa para ler a média salarial dos funcionários e, na sequência, o nome e o salário de um dos funcionários dessa empresa. Ao terminar a leitura, exibir o nome do funcionário e se o seu salário é maior, menor ou igual a média salarial.

media_salarial = float(input(""))
nome_funcionario = str(input(""))
salario_funcionario = float(input(""))

resultado = salario_funcionario - media_salarial

if salario_funcionario > media_salarial:
    print(f"{nome_funcionario} recebe R$ {resultado:.2f} a mais do que a média salarial da empresa.")
elif salario_funcionario < media_salarial:
    print(f"{nome_funcionario} recebe R$ {resultado:.2f} a menos do que a média salarial da empresa.")
elif salario_funcionario == media_salarial:
    print(f"{nome_funcionario} recebe igual a média salarial da empresa.")