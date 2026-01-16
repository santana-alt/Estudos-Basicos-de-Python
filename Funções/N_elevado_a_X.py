#Escreva uma função que receba dois parâmetros: numero e potencia. O retorno dessa função deve ser o numero elevado à potência

def numero_e_potencia():
    numero = float(input(""))
    potencia = int(input(""))
    resultado = numero**potencia
    return  resultado
print(f"{numero_e_potencia():.2f}")