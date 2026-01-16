#Faça um programa que, dado os parâmetros base e altura, crie uma função que calcule a área de um retângulo.

def area_retangulo(base,altura):
    return base * altura
base = float(input(""))
altura = float(input(""))

resultado = area_retangulo(base,altura)
print(f"A área do retângulo é {resultado:.2f}")