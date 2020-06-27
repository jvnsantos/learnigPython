# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias.

metros = float(input("Informe o tamanho em M² da area a ser pintada: "))

litro = metros/6 #litros utilizados
litroTotal = litro
galao = 0
lata = 0

escolha = int(input("""
1 - APENAS LATAS (18 L)
2 - APENAS GALOES (3.6 L)
3 - MISTURAR GALOES E TINTAS
"""))

if escolha == 1: # CASO SEJA SÓ LATAS DE 18L
    if litro > 18:
        while not litro <= 0:
            litro = litro - 18
            lata += 1
    else: lata = 1

    custo = lata * 80.00

    print("\nserá necessário ", litroTotal, ' litros para pintar esta area')
    print("Será necessário a compra de ",lata," galoês")
    print("O valor total será de R$",custo)





if escolha == 2: # CASO SEJA SÓ GALOES DE 3,6L

    if litro > 3.6:

        while not litro <= 0:
            litro = litro - 3.6
            galao += 1

    else: galao = 1

    custoGalao = galao * 25.00

    print("será necessário ", litroTotal, ' litros para pintar esta area')
    print("\nSerá necessário a compra de ",galao," latas")
    print("O valor total será de R$",custoGalao)






if escolha == 3: # CASO SEJA MISTURADO
    if litro > 18:

        while not litro <= 18:
            litro = litro - 18
            lata += 1
        while not litro <= 3.6:
            litro = litro - 3.6
            galao += 1

        while not litro <= 0:
            litro = litro - 3.6
            galao += 1

    else:
        lata += 1

    custoGalao = galao * 25.00
    custoLata = lata * 80.00
    custoTotal = custoGalao + custoLata

    print("\nserá necessário ", litroTotal,' litros para pintar esta area' )
    print("Será necessário a compra de: ")
    print( lata , 'latas')
    print(galao , 'galoes')

    print("O valor total será de R$", custoTotal)



