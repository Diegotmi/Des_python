imposto = float(input('Valor percentual do imposto:'))
if imposto < 10 :
    print("Médio")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito Alto")

