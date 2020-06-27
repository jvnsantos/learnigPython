#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#Formula A = PI * r²

raio = float(input("Qual o raio do circulo? "))

# pode ser feito assim
# area = 3.14 * (raio * raio)

# Ou assim com dois asteriscos, significa ao quadrado, ao cubo seria ** 3 e por ai vai. =)
area = 3.14 * (raio ** 2)

print("Area = ",area)