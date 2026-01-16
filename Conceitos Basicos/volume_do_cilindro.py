#Faça um programa que, solicite a altura e o raio de um cilindro, calcule o volume total do cilindro (use π=3.14) e exiba esse valor.

ALTURA = float(input(""))
RAIO = float(input(""))

VOLUME = 3.14 * RAIO**2 * ALTURA


print(f"O volume do cilindro que tem {ALTURA} de altura e {RAIO} de raio é igual a {VOLUME:.2f}")