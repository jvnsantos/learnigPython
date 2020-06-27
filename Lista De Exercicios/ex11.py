#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

intnum1 = int(input("Primeiro numero inteiro: "))
intnum2 = int(input("Segundo numero inteiro: "))
floatnum = float(input("Agora um numero real"))

produto1 = (intnum1 * 2) + (intnum2 / 2)

produto2 = (intnum1 * 3) + floatnum

produto3 = floatnum ** 3

print("\n A) O produto do dobro do primeiro com metade do segundo: ", produto1)
print("\n B) O produto da soma do triplo do primeiro com o terceiro: ", produto2)
print("\n C) O terceiro elevado ao cubo: ", produto3)