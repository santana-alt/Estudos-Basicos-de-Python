#Escreva um programa para ler um ÚNICO caractere e depois informar se este é uma vogal, um número ou uma operação matemática (+, -, * ou /).

caractere = str(input(""))

if caractere.isnumeric():
  print(f"O caractere é um número")
elif (caractere == "+") or (caractere == "-") or (caractere == "/") or (caractere == "*"):
  print(f"O caractere é uma operação matemática")
elif (caractere == "a") or (caractere == "e") or (caractere == "i") or (caractere == "o") or (caractere == "u") or (caractere == "A") or (caractere == "E") or (caractere == "I") or (caractere == "O") or (caractere == "U"):
  print(f"O caractere é uma vogal")