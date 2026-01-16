#Faça um programa que, dado uma string, crie uma função que conta quantas vezes cada vogal aparece na string. Obs.: letras maiusculas e minusculas são consideradas, mas letras acentuadas não são.
#A saída deverá ser um dicionário, onde a chave corresponde a vogal e o valor é a quantidade de vezes que aquela vogal apareceu na variável word.

palavra = str(input(""))
def contar_vogais(palavra):
    palavra = palavra.lower()
    contagem = {
        "a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0
    }

    for x in palavra:
        if x in contagem:
            contagem[x] += 1
    return contagem
print(contar_vogais(palavra))