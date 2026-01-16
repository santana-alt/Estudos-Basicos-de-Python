#Escreva um programa para ler o tamanho de três segmentos de retas e informar se estas podem formar um triângulo (a soma de quaisquer dois lados sempre deve ser maior que o terceiro lado).

#Caso sim, também deve-se informar se este é equilátero (tem os três lados iguais), escaleno (tem os três lados diferentes) ou isósceles (tem apenas dois lados iguais).

lado_1 = int(input(""))
lado_2 = int(input(""))
lado_3 = int(input(""))

if lado_1 == lado_2 == lado_3:
    print("Triangulinho com todos os lados iguais: é equilátero!!")
elif (lado_1 + lado_2 < lado_3) or (lado_2 + lado_3 < lado_1 ) or (lado_3 + lado_1 < lado_2):
    print("Esses segmentos de reta não formam um triângulo. Tchau!!!!")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_1 or lado_2 == lado_3 or lado_3 == lado_1 or lado_3 == lado_2:
    print("Triangulinho com dois lados iguais: é isósceles!!")
elif lado_1 != lado_2 != lado_3:
    print("Tem os três lados diferentes mas ainda continua sendo um triangulinho: é escaleno!!")
else:
    print("Tem os três lados diferentes mas ainda continua sendo um triangulinho: é escaleno!!")