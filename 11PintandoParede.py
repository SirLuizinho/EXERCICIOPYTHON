largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

area = largura * altura

print(f"Sua parede tem a dimensão de {largura:.2f}x{altura:.2f}, e sua área é de {area:.2f}m²")
print(f"Para pintar essa parede, você precisará de {area/2:.2f} litros de tinta")