#Faça um programa que, dado uma string, conte a quantidade de vogais que aparecem naquela palavra. Obs.: letras maiusculas e minusculas devem ser consideradas, mas letras acentuadas não.

def contar_vogais(palavra):
    vogais = ["a","e","i","o","u"]
    palavra = palavra.lower()
    contagem = 0

    for letras in palavra:
        if letras in vogais:
            contagem += 1
    return contagem
palavra = str(input(""))
resultado_contagem = contar_vogais(palavra)
print(f"A quantidade de vogais em {palavra} é {resultado_contagem}")