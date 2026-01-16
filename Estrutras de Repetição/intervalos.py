#Faça um programa para ler o primeiro e último número de uma sequência e depois exibir: a somatória desses dois números, os números pares e os números ímpares dentro desse intervalo da sequência.

primeiro = int(input(""))
segundo = int(input(""))

soma = primeiro + segundo
print(f"A soma dos números é: {soma}\n")

print(f"Os números pares dentro da sequência são:")
for numero in range(primeiro, segundo +1):
    if numero % 2 == 0:
        print(f"{numero}")

print(f"\nOs números ímpares dentro da sequência são:")
for numero in range(primeiro, segundo +1):
    if numero % 2 != 0:
        print(f"{numero}")