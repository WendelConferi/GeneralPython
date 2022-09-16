Dias = int(input('Por quantos dias o carro foi alugado? '))
Km = float(input('Quantos quilômetros ele percorreu? '))
Preço = (Dias*60)+(Km*0.15)
print(f'Tendo o carro sido alugado por {Dias:.1f} dias e percorrido {Km:.2f} km, o preço a ser pago é de R${Preço:.2f}! ')