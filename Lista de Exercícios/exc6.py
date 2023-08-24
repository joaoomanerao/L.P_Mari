#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
#comprar.
#Considere: US$ 1.00 = R$ 5.41

real = float(input("Digite seu dinheiro em reais: "))
dolar = real / 5.41

print( f"Você pode comprar {dolar} dólares")
