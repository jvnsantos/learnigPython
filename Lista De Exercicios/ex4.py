#Faça um Programa que peça as 4 notas bimestrais e mostre a média

nota1 = float(input("PROVA AVALIATIVA 1 = "))
nota2 = float(input("PROVA AVALIATIVA 2 = "))
nota3 = float(input("TRABALHO BIMESTRAL = "))
nota4 = float(input("ATIVIDADES EM SALA = "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A MÉDIA DO BIMESTRE FOI: ", media)
#A VIRGULA NAO FUNCIONA, NESTE CASO SE O NUMERO FOR DECIMAL NECESSITA UTILIZAR O PONTO " . " PARA FUNCIONAR. 