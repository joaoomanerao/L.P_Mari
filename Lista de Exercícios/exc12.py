"""  
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero. """

eleitores = int(input("Diga o número de pessoas que vão participar da votação: "))
for i in range (eleitores):
    voto = int(input("Em qual das opções você deseja votar? \n João - 1 \n Michael - 2 \n Jordan - 3 \n Poggers - 4 \n Nulo - 5 \n Branco - 6 "))
    