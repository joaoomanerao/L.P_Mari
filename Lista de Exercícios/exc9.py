#Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
#mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
#Euros.

real = float(input("Quanto dinheiro você possui em reais? "))

dolar = real / 4.87
euro = real / 5.27

print( f"Você possui {dolar} dólares e {euro} euros")