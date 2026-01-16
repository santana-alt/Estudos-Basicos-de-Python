#Escreva um programa que, leia um valor de custo e o percentual de lucro desejado, e na sequencia mostre o valor final do produto;

custo = float(input(""))
percentual = float(input(""))

valor_final = custo + (custo * percentual) / 100

print(f"Valor final do produto: R$ {valor_final:.4f}.")