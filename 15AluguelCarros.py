dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos KM rodados? "))

preço = (dias * 60) + (km * 0.15)

print(f"O valor total a se pagar por este aluguel é: R${preço:.2f}")