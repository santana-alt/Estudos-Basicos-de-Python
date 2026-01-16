#Escreva um programa que permute (troque) o valor de duas variáveis inteiras.

a = input("")
b = input("")
 
temporaria=a
a=b
b=temporaria
 
print(f"Valor de a após permutação: {a}")
print(f"Valor de b após permutação: {b}")