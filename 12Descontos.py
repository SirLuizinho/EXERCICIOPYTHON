pre = float(input("Qual o valor inicial do produto? R$ "))
desconto = (5 / 100) * pre
preatualizado = pre - desconto

print(f"O valor deste produto com 5% de desconto vai de R${pre:.2f} para R${preatualizado:.2f}")