#O programa deve calcular e exibir: A quantidade de ingressos meia-entrada e inteiros vendidos;O valor faturado com cada tipo de ingresso;O valor total arrecadado com as vendas.

total_ingressos = int(input(""))
total_meia = int(input(""))
valor_ingresso = float(input(""))

qntd_meia = int((total_meia / 100) * total_ingressos)
total_inteira = total_ingressos - qntd_meia

valor_meia = valor_ingresso / 2
faturamento_meia = qntd_meia * valor_meia
faturamento_inteira = total_inteira * valor_ingresso
faturamento_total = faturamento_meia + faturamento_inteira

print(f"Quantidade de ingressos meia-entrada: {qntd_meia}")
print(f"Quantidade de ingressos inteiros: {total_inteira}")
print(f"Faturamento com meia-entrada: R${faturamento_meia:.2f}")
print(f"Faturamento com inteira: R${faturamento_inteira:.2f}")
print(f"Faturamento total: R${faturamento_total:.2f}")
