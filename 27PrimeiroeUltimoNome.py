nome = str(input("Digite seu nome completo: ")).upper()
nomeseparado = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nomeseparado[0]}')
print(f'E seu último nome é {nomeseparado[-1]}')