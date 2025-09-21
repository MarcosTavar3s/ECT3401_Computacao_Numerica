import math
import numpy as np
import base_n

bases = list(range(2,27))

print(bases)
print('Olá! Seja bem-vind@ ao conversor de bases numéricas')
print('-------------------------------------------------------------------------------------------\n')
print('Esse programa foi desenvolvido por Marcos Aurélio para a disciplina de Computação Numérica!\n')
print('-------------------------------------------------------------------------------------------\n')

print('Preenchimento dos números')
numero_base_1 = input('Digite o numero: ')
base_origem = int(input('Digite a base do numero inserido: '))

while not bases.count(base_origem):
    base_origem = int(input('A base que você inseriu não está contida no escopo deste programa! Tente novamente!\nAs bases disponíveis são de 2 a 26: '))

base_destino =  int(input('Digite a base a qual você deseja converter: '))

while not bases.count(base_destino):
    base_destino = int(input('A base que você inseriu não está contida no escopo deste programa! Tente novamente!\nAs bases disponíveis são de 2 a 26: '))

if base_origem == base_destino:
    print(f'As bases são iguais, assim, o número será o mesmo: {numero_base_1}')
    exit()
  
print('\n-------------------------------------------------------------------------------------------\n')
print('Aplicando o método de Horner...\n')
print('-------------------------------------------------------------------------------------------\n')
  
n = 0 
numero_em_polinomio = ''

for i in range(len(numero_base_1)):
    if len(numero_base_1) - (i+1):
        numero_em_polinomio += f'{numero_base_1[i]}*{base_origem}**{len(numero_base_1) - (i+1)} + '
        
    else:
        numero_em_polinomio += f'{numero_base_1[i]} * {base_origem} ** {len(numero_base_1) - (i+1)}'
    n += 1

print(f'Escrevendo o numero na base {base_origem} como polinômio: {numero_em_polinomio}\n')

print('-------------------------------------------------------------------------------------------\n')

print(f'Transformando cada termo de {numero_em_polinomio} para a base de destino {base_destino}\n')
print(base_n.transforma_polinomio(numero_em_polinomio, base_destino))
