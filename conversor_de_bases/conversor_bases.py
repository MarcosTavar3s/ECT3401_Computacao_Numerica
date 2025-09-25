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

print('O que voce deseja fazer? Digite o número correspondente para a operação')
print('-------------------------------------------------------------------------------------------\n')
print('1 - Conversão entre bases')
print('2 - Soma em um base n')
print('3 - Multiplicação em uma base n')
print('OBS: Bases disponíveis vão de 2 até 26 (P)')
print('-------------------------------------------------------------------------------------------')

operacao = int(input("Digite a operação escolhida: "))

if operacao == 1:
    print('\n-------------------------------------------------------------------------------------------\n')
    print('Conversão de bases selecionada com sucesso\n')
    print('-------------------------------------------------------------------------------------------\n')

    print('Preenchimento dos números')
    base_origem = int(input('Digite a base do numero inserido: '))

    while not bases.count(base_origem):
        base_origem = int(input('A base que você inseriu não está contida no escopo deste programa! Tente novamente!\nAs bases disponíveis são de 2 a 26: '))

    base_origem_simbolos = list(simbolos[:base_origem])

    numero_base_1 = input('Digite o numero: ').upper()

    while not metodo_alternativo.valida(numero_base_1, base_origem):
        numero_base_1 = input('O número escolhido está fora do escopo da base! Tente novamente!\n')
        
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

    print(f"Número convertido após sucessivas somas feitas nas base {base_destino} será:")
    metodo_alternativo.converte(numero_base_1, base_origem, base_destino)
    print('-------------------------------------------------------------------------------------------\n')
    
elif operacao == 2:
    print('-------------------------------------------------------------------------------------------\n')
    print('Operação de soma selecionada com sucesso\n')
    print('-------------------------------------------------------------------------------------------\n')
    base = int(input('Digite a base: '))
    n1 = input('Digite o numero 01: ')

    while not metodo_alternativo.valida(n1, base):
        n1 = input(f'O número escolhido está fora do escopo da base {base}! Tente novamente!\n')

    n2 = input('Digite o numero 02: ')
    while not metodo_alternativo.valida(n1, base):
        n1 = input(f'O número escolhido está fora do escopo da base {base}! Tente novamente!\n')

    
    print('-------------------------------------------------------------------------------------------\n')
    print(f"Resultado obtido após a aplicação de somas na base {base} será: ")
    # print(base_n.soma_em_base_n(n1, n2, base))
    print(metodo_alternativo.soma_em_base_n(n1, n2, base) + f' (base {base})')
    print('-------------------------------------------------------------------------------------------\n')
    

elif operacao == 3:
    print('-------------------------------------------------------------------------------------------\n')
    print('Operação de multiplicação selecionada com sucesso\n')
    print('-------------------------------------------------------------------------------------------\n')
    base = int(input('Digite a base: '))
    
    n1 = input('Digite o numero 01: ')
    while not metodo_alternativo.valida(n1, base):
        n1 = input(f'O número escolhido está fora do escopo da base {base}! Tente novamente!\n')
        
    n2 = input('Digite o numero 02: ')
    while not metodo_alternativo.valida(n2, base):
        n2 = input(f'O número escolhido está fora do escopo da base {base}! Tente novamente!\n')


    # print(base_n.multiplica_em_base_n(n1, n2, base) + f' (base {base})')
    print(metodo_alternativo.multiplica_em_base_n(n1, n2, base) + f' (base {base})')
    print('-------------------------------------------------------------------------------------------\n')
