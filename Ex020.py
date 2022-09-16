import random
nome1 = input('O nome do primeiro aluno: ')
nome2 = input('O nome do segundo aluno: ')
nome3 = input('O nome do terceiro aluno: ')
nome4 = input('O nome do quarto aluno: ')
lista = (nome1, nome2, nome3, nome4)
sorteio = random.sample(lista, 4)
print(f'A ordem de apresentação dos alunos deve ser {sorteio}.')
