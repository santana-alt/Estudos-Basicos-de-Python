#Crie um programa que receba uma temperatura em Celsius e exiba a temperatura lida usando as escalas Kelvin (K) e Fahrenheit (F).

temperatura_celsius = float(input(""))

temperatura_kelvin = temperatura_celsius+273
temperatura_fahrenheit = (1.8*temperatura_celsius)+32

print(f"Temperatura em Kelvin: {temperatura_kelvin:.2f}K")
print(f"Temperatura em Fahrenheit: {temperatura_fahrenheit:.2f}ºF")