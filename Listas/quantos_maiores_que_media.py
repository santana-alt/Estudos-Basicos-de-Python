#Dada uma lista de n números, calcule a média aritmética e conte quantos elementos são maiores do que ela. Os elementos da lista devem ser recebidos em uma única linha, separados por um espaço em branco, e devem ser convertidos para inteiro posteriormente.
#Os elementos da lista devem ser recebidos em uma única linha, separados por um espaço em branco, e devem ser convertidos para inteiro posteriormente.

elementos = list(map(int,input().split()))

media_elementos = sum(elementos) / len(elementos)

maior_media = sum(1 for n in elementos if n > media_elementos)
print(f"{maior_media:.0f}")