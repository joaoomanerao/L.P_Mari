#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
#de aumento.

preco = float(input("Digite o preço de um produto: "))

des = preco / 100 * 5
conto = preco - des 

au = preco / 100 * 15
mento = preco + au

print ( f"O preço do seu produto com 5% de desconto é de {conto}, e com 15% de aumento é de {mento}")