dinheiro = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = dinheiro * 5.16
euro = dinheiro * 5.09
print(f"Convertendo R${dinheiro:.2f} em dólar, você tem U${dolar:.2f}")
print(f"Convertendo R${dinheiro:.2f} em euro, você tem £{euro:.2f}")