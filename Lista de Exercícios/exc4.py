#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre
#ele

a = input("Digite algo: ")

print(a.isnumeric())
print(a.isalpha())
print(a.isascii())
print(a.isalnum())
print(a.islower())
print(a.isupper())
print(a.istitle())
print(a.isspace())