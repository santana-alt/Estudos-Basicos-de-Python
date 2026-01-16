#Escreva um programa que, a partir de um valor de custo e de um valor de venda, mostre o valor do lucro obtido com a venda do produto.

custo = float(input(""))
venda = float(input(""))

lucro = venda - custo

print(f"O lucro obtido foi R$ {lucro:.2f}.")