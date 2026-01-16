#Faça um programa que, dado um saldo inicial, simule operações de depositar ou sacar.
#Enquanto o usuário não colocar como entrada "sair" na * operacao *, o programa deverá ser capaz de executar as operação de depositar ou sacar.
#Obs.: a operação de depositar só será feita se a variável operacao for "depositar" e a operação de sacar só será feita se a variável operacao for sacar.
#Após verificar se a operação é válida ou não, seu programa deve receber o valor (float) que será depositado/sacado.

saldo = float(input(""))
saldo_anterior = saldo

while True:
    operacao = str(input(""))

    if operacao == "depositar":
        dinheiro = float(input(""))
        saldo += dinheiro
        saldo_atual = saldo
    elif operacao == "sacar":
        dinheiro = float(input(""))
        saldo -= dinheiro
        saldo_atual = saldo
    elif operacao == "sair":
        break
    else:
        print("digite se quer depositar, sacar ou sair!")
print(f"Seu saldo era: R$ {saldo_anterior:.2f}")   
print(f"Seu novo saldo é: R$ {saldo_atual:.2f}") 