import math
import numpy as np
import base_n
import metodo_alternativo

bases = list(range(2,27))
# conjunto de caracteres possiveis no pior caso (base 26)
simbolos = "0123456789ABCDEFGHIJKLMNOP" 

print(bases)
print('Olá! Seja bem-vind@ ao conversor de bases numéricas')
print('-------------------------------------------------------------------------------------------\n')
print('Esse programa foi desenvolvido por Marcos Aurélio para a disciplina de Computação Numérica!\n')
print('-------------------------------------------------------------------------------------------\n')

print('Preenchimento dos números')
base_origem = int(input('Digite a base do numero inserido: '))

while not bases.count(base_origem):
    base_origem = int(input('A base que você inseriu não está contida no escopo deste programa! Tente novamente!\nAs bases disponíveis são de 2 a 26: '))

base_origem_simbolos = list(simbolos[:base_origem])

numero_base_1 = input('Digite o numero: ').upper()

numero_valido = True

for i in numero_base_1:
    if not base_origem_simbolos.count(i):
        numero_valido = False

while not numero_valido:
    numero_base_1 = input('O número escolhido está fora do escopo da base! Tente novamente!\n')
    
    for i in numero_base_1:
        if not base_origem_simbolos.count(i):
            numero_valido = False


base_destino =  int(input('Digite a base a qual você deseja converter: '))

while not bases.count(base_destino):
    base_destino = int(input('A base que você inseriu não está contida no escopo deste programa! Tente novamente!\nAs bases disponíveis são de 2 a 26: '))

if base_origem == base_destino:
    print(f'As bases são iguais, assim, o número será o mesmo: {numero_base_1}')
    exit()
  
print('\n-------------------------------------------------------------------------------------------\n')
print('Aplicando o algoritmo...\n')
print('-------------------------------------------------------------------------------------------\n')
  
n = 0 
numero_em_polinomio = ''

for i in range(len(numero_base_1)):
    if len(numero_base_1) - (i+1):
        numero_em_polinomio += f'{numero_base_1[i]}*{base_origem}**{len(numero_base_1) - (i+1)} + '
        
    else:
        numero_em_polinomio += f'{numero_base_1[i]}*{base_origem}**{len(numero_base_1) - (i+1)}'
    n += 1

print(f'Escrevendo o numero na base {base_origem} como polinômio: {numero_em_polinomio}\n')

print('-------------------------------------------------------------------------------------------\n')

print(f'Transformando cada termo de {numero_em_polinomio} para a base de destino {base_destino}\n')

print('-------------------------------------------------------------------------------------------\n')

print(f"Número convertido após sucessivas multiplicações e somas feitas na base {base_destino} será:")
base_n.converte_bases(numero_base_1, base_origem, base_destino)
print('-------------------------------------------------------------------------------------------\n')

print(f"Número convertido após sucessivas somas feitas nas base {base_destino} será:")
metodo_alternativo.converte(numero_base_1, base_origem, base_destino)
print('-------------------------------------------------------------------------------------------\n')
