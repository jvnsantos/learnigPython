# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import time

def calc():
    op = input("ESCOLHA ENTRE CM OU M: ")

    if (op == "CM" or "cm"):
        lado = float(input("Informe o tamnho do lado do quadrado: "))
        area = lado ** 2
        print("A area deste quadrado é de ",area," cm")

    elif (op == "M" or "m"):
        lado = float(input("Informe o tamnho do lado do quadrado: "))
        area = lado ** 2
        print("A area deste quadrado é de ",area," m")

    else:
        print("Deve ser informado a unidade de medida em um destes formatos (M ou CM) ")
        time.sleep(2)
        calc()

calc()
