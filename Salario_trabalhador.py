#Um empresa contrata um encanador a R$ 20,00 por dia.
#Crie um programa que solicite o número de dias trabalhados e retorne o valor do salário a ser pago.

dia_encanador = 20.0
dias_trabalhados = int(input('Insira a quantidade de dias trabalhados:'))
valor_total = dia_encanador *dias_trabalhados
print('Valor total a receber é:',valor_total)