#Faça um programa que receba 10 números digitados pelo usuário e, em seguida, leia um expoente. O programa deve criar e imprimir uma nova lista com cada número elevado ao expoente informado.

lista_numeros = []

numero1 = float(input(""))
lista_numeros.append(numero1)
numero2 = float(input(""))
lista_numeros.append(numero2)
numero3 = float(input(""))
lista_numeros.append(numero3)
numero4 = float(input(""))
lista_numeros.append(numero4)
numero5 = float(input(""))
lista_numeros.append(numero5)
numero6 = float(input(""))
lista_numeros.append(numero6)
numero7 = float(input(""))
lista_numeros.append(numero7)
numero8 = float(input(""))
lista_numeros.append(numero8)
numero9 = float(input(""))
lista_numeros.append(numero9)
numero10 = float(input(""))
lista_numeros.append(numero10)

expoente = int(input(""))

nova_lista_numeros = [x ** expoente for x in lista_numeros]
for x in nova_lista_numeros:
    print(f"{x:.2f}")