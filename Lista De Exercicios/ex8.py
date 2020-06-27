#Faça um Programa que pergunte quanto você ganha por hora e o número
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input("Quanto voce ganha por hora? "))
horasTrabalhadas = float(input("Quantas horas voce trabalha por mês? "))

total = valorHora * horasTrabalhadas

print("Em um mês de trabalho o salario é de: ", total)