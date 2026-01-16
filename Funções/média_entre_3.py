#Escreva uma função chamada media(a, b, c) que recebe três números como argumentos e retorna a média aritmética entre eles. A saída deverá ser a média aritmética entre os três números, com duas casas decimais.

def media(a,b,c):
    return (a+b+c) / 3
n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))

resultado_media = media(n1,n2,n3)    
print(f"{resultado_media:.2f}")