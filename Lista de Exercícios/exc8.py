#Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
#quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

alt = float(input("Digite a altura da sua parede: "))
larg = float(input("Digite a largura da sua parede: "))

area = alt * larg

# 1litro = 2m²

tinta = area / 2

print( f"A área do seu local é {area} m², e a quantidade de tinta que você precisará para pintar é de {tinta}")