# Receba código da peça
# Receba valor da peça
# Receba Quantidade de peças
# Calcule o valor total da peça (Quantidade * Valor da peça)
# Mostre o código da peça e seu valor total


codigo_peca = input('Insira codigo da peça:')
valor_peca = input('Insira o valor da peça:')
qtd_peca = input('Insira a quantidade de peças:')

peca_estoque = float(valor_peca) * int(qtd_peca)

print('Codigo da peça:' + codigo_peca + '\n''Valor Total:', peca_estoque)


