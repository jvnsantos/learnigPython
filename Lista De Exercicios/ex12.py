#Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Qual a altura em metros? "))

formula = (72.7 * altura) - 58

print("\n O peso ideal seria de: ",formula," kg")