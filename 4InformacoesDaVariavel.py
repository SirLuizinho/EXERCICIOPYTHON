var = input("Digite algo: ")
print("O tipo primitivo dessa variável é", type(var))
print("Só tem espaços?", var.isspace())
print("É um número?", var.isnumeric())
print("É alfabético?", var.isalpha())
print("É alfanumérico?", var.isalnum())
print("Está em maiúsculas?", var.isupper())
print("Está em minúsculas?", var.islower())
print("Está capitalizada?", var.istitle())