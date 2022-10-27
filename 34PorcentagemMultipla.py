salario = float(input("Qual o salário do funcionário? R$"))

if salario > 1250:
    aumento = salario * (15 / 100)
    salarioatt = salario + aumento
else:
    aumento = salario * (15 / 100)
    salarioatt = salario + aumento

print(f'O salário do funcionário passou de R${salario:.2f} para R${salarioatt:.2f}')