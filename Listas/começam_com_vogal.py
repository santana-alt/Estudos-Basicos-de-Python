#Dado uma lista de palavras, crie uma nova lista contendo apenas as que começam com vogal
#A saída deverá ser todas as palavras digitadas pelo usuário que COMEÇAM com vogais, sendo exibidas linha a linha, de acordo com a ordem de entrada.Se caso todas as palavras digitadas não começarem com vogal, o programa deverá exibir:
#"Nenhuma palavra digitada começa com vogal."

palavra = str(input())
lista = []
lista_vogal = []

while palavra != "fim":
    lista.append(palavra)
    palavra = str(input())
for a in lista:
    if a[0].lower() in "aeiou":
        lista_vogal.append(a)
if not lista_vogal:
        print("Nenhuma palavra digitada começa com vogal.")
else:
    for i in lista_vogal:
         print(i)