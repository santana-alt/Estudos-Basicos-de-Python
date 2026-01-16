#Faça um programa que leia os nomes (sem repetição), os preços de compra e os percentuais de lucro de 5 produtos. Após a leitura, exiba para cada produto seu nome, o preço de compra e o preço de venda calculado.

lista_produto = []
lista_preco = []
lista_lucro = []

for i in range(5):
    nomes_produto = str(input())
    preco_compra = float(input())
    percentual_lucro = float(input())

    lucro = preco_compra * (percentual_lucro/100)
    venda = preco_compra + lucro    

    lista_produto.append(nomes_produto)
    lista_preco.append(preco_compra)
    lista_lucro.append(venda)

lista_combinada = zip(lista_produto,lista_preco, lista_lucro)
for nomes_produto, preco_compra, preco_venda in lista_combinada:
    print(f"{nomes_produto}: Compra = R${preco_compra:.2f}, Venda = R${preco_venda:.2f}")