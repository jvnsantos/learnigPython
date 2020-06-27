#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = input("Voce é Homem ou Mulher? Responda com 'M' ou 'F' ").upper()# Transforma o minusculo em maiusculo

if sexo == 'M':

    altura = float(input("Moço qual a altura? A virgula é ponto  "))
    formula = (72.7 * altura ) - 58
    print("Lindão, seu peso ideal seria de: ", round(formula,2),"kg")

elif sexo == 'F' :

    altura = float(input("Moça qual a altura? A virgula é ponto  "))
    formula = (62.1 * altura) - 44.7
    print("Linda, seu peso ideal seria de: ", round(formula,2), "kg")