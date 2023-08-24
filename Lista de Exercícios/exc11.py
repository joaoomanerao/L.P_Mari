#Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado.

def main():
    global salario
    salario = NumHoras * ValHoras
    global conto
    conto = salario - (salario*0.02)
    return salario, conto

nome = str(input("Digite seu nome: "))
NumHoras = int(input("Digite o números de horas trabalhadas: "))
ValHoras = float(input("Digite o valor da hora trabalhada: "))

main()
print( f"{nome}, seu salário final é de {conto}")