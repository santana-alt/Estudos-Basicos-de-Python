#Faça um programa que leia o nome, o sobrenome e a idade de um atleta e exiba seu nome completo e se ele está na categoria infantil (menor de 12 anos), juvenil (entre 12 e 17 anos), adulto (entre 18 e 35 anos) ou master (acima de 35 anos).

nome = str(input(""))
sobrenome = str(input(""))
idade = int(input(""))

nome_completo = nome + " " + sobrenome

if idade < 12:
  print(f"A categoria do atleta {nome_completo} é a infantil.")
elif (idade >= 12) and (idade <= 17):
  print(f"A categoria do atleta {nome_completo} é a juvenil.")
elif (idade >=18) and (idade <= 35):
  print(f"A categoria do atleta {nome_completo} é a adulta.")
elif idade > 35:
  print(f"A categoria do atleta {nome_completo} é a master.")
  
