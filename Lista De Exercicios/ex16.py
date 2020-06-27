# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros = float(input("Informe o tamanho em M² da area a ser pintada: "))

litro = metros/3 #litros utilizados
galao = 0

if litro > 18:
    while not litro <= 18:
        litro = litro - 18
        galao += 1

else:
    galao = 1

custo = galao * 80.00


print("\nSerá necessário a compra de ",galao," galoês")
print("O valor total será de R$",custo)
