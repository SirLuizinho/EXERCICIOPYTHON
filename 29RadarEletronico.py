vel = float(input('Qual é a velocidade atual do carro? '))

if vel <= 80:
    print('\033[33;1mTenha um BOM DIA e dirija com segurança!')
else:
    acima = vel - 80
    print(f'\033[31;1mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa no valor de R${7 * acima}')
    print('\033[33;1mTenha um BOM DIA e dirija com segurança!')