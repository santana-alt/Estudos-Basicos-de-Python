#Escreva um programa que recebe uma única frase como entrada e conta quantas vezes cada letra do alfabeto aparece, ignorando espaços, acentos e letras maiúsculas/minúsculas. Exiba as letras e suas contagens em ordem alfabética.

frase = str(input()).lower()
dicionario = {
    "A":0,
    "B":0,
    "C":0,
    "D":0,
    "E":0,
    "F":0,
    "G":0,
    "H":0,
    "I":0,
    "J":0,
    "K":0,
    "L":0,
    "M":0,
    "N":0,
    "O":0,
    "P":0,
    "Q":0,
    "R":0,
    "S":0,
    "T":0,
    "U":0,
    "V":0,
    "W":0,
    "X":0,
    "Y":0,
    "Z":0,
    "Á":0,
    "É":0,
    "Í":0,
    "Ó":0,
    "Ú":0,
    "Ã":0,
    "Ç":0
}
for letras in frase:
    letras = letras.upper()
    if letras in dicionario:
        dicionario[letras] += 1

for letra,contagem in sorted(dicionario.items()):
  if contagem > 0:
     print(f"{letra}: {contagem}")