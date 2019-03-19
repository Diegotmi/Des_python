# Faça um algoritmo para “Calcular o estoque médio de uma peça”,
# sendo que ESTOQUEMÉDIO = (QUANTIDADE MÍNIMA + QUANTIDADE MÁXIMA) /2

codigo_peca = input('Insira codigo da peça:')
qtd_min = int(input('Insira quantidade minima de peças:'))
qdt_max = int(input('Insira quantidade maxima de peças:'))

estoque_medio = (qtd_min + qdt_max) / 2

print('Estoque médio é :',estoque_medio)