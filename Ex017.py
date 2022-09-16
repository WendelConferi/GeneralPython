import math
ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o catato oposto: '))
#h = math.sqrt((ca*ca)+(co*co))
h = math.hypot(ca, co)
print(f'Calculando o cateto adjacente {ca} e o cateto oposto {co}, o valor da hipotenusa é de {h:.2f}')
