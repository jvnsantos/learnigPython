#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

F = float(input("Informe os graus em F: "))
C = (5* (F-32) / 9)

# round (numero , quantidade de virgulas a´pos o ponto)
print("Em C: ", round(C , 2))

