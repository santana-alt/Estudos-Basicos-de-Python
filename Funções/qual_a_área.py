#Crie uma função area_retangulo(base, altura) que calcule e retorne a área de um retângulo. 

def area_retangulo(base,altura):
    return base * altura
base = float(input(""))
altura = float(input(""))

area = area_retangulo(base,altura)
print(f"A área do retângulo é {area:.2f}")