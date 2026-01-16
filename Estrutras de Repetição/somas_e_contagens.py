#Faça um programa para ler números inteiros e positivos até o usuário não desejar continuar informando um novo número. Ao final, o programa deve exibir o total de números lidos e a soma deles.

confirmacao = str(input()).upper()
soma = 0
quantidade = 0
while confirmacao == "S":
    numero = float(input())
    if numero > 0:
        soma += numero
        quantidade += 1
    else:
        print("Digite numeros positivos!")
    confirmacao = str(input()).upper()
print(f"Você digitou {quantidade} números")
print(f"A soma final é: {soma:.2f}")