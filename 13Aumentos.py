sal = float(input("Qual o salário do funcionário? R$ "))
aumento = (15/100) * sal
salatualizado = sal + aumento

print(f"O salário desse funcionário vai de R${sal:.2f} para R${salatualizado:.2f}.")