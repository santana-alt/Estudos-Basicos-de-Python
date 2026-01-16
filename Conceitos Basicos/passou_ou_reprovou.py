#Escreva um programa que leia as 2 notas de um aluno em uma disciplina, depois exiba quantos pontos o aluno ficou distante da nota 10 para cada avaliação, sua média e quantos pontos a média do aluno ficou distante da nota 10.

Nota1 = float(input(""))
Nota2 = float(input(""))

distancia_nota1 = 10 - Nota1
distancia_nota2 = 10 - Nota2
media = (Nota1 + Nota2) / 2
distancia_media = 10 - media

print(f"{distancia_nota1}")
print(f"{distancia_nota2}")
print(f"{media}")
print(f"{distancia_media}")