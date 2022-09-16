n = input('Quanto é X+Y? ')
print('Qual é o seu tipo?', type(n))
print('É um alfanúmerico?', n.isalnum())
print('É alfábetico?', n.isalpha())
print('É um número?', n.isnumeric())
print('É um dígito?', n.isdigit())
print('Está em minísculo? ',n.islower())
print('Só tem espaços? ',n.isspace())
print('Está capitalizada? ',n.istitle())
print('Está em maíusculo? ',n.isupper())
#Ordem de Precedência
#1 - ()
#2 - **
#3 - *,/,//,%
#4 - +,-