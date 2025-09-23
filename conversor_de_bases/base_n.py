# converte caractere para valor 
def char_valor(c: str) -> int:
    if c.isdigit():
        return int(c)
    return ord(c.upper()) - ord('A') + 10

# converte valor para caractere
def valor_char(n: int) -> str:
    if n < 10:
        return str(n)
    return chr(ord('A') + n - 10)

# soma duas strings representando números em base n
def soma_em_base_n(e1: str, e2: str, base: int) -> str:
    e1 = list(e1.upper())
    e2 = list(e2.upper())

    tamanho_1 = len(e1)
    tamanho_2 = len(e2)

    # supondo que e1 sempre vai ser o maior
    if tamanho_1 < tamanho_2:
        e1, e2 = e2, e1
        tamanho_1, tamanho_2 = tamanho_2, tamanho_1

    # padroniza tamanho do menor número
    e2 = ['0'] * (tamanho_1 - tamanho_2) + e2

    resultado = []
    cin = 0

    for i in range(tamanho_1 - 1, -1, -1):
        s = char_valor(e1[i]) + char_valor(e2[i]) + cin
        cin = s // base
        resultado.append(valor_char(s % base))

    if cin > 0:
        resultado.append(valor_char(cin))

    # retorna uma string
    return ''.join(resultado[::-1])

# multiplica dois numeros desde que o numerador seja de um digito
def multiplica_um_digito(e1: str, d: str, base: int) -> str:
    qtd_somas = char_valor(d)
    resultado = '0'
    
    for _ in range(qtd_somas):
        resultado = soma_em_base_n(resultado, e1, base)
        
    return resultado

# multiplicacao de dois numeros quaisquer em base n
def multiplica_em_base_n(e1: str, e2: str, base: int) -> str:
    e1 = e1.upper()
    e2 = e2.upper()
    resultados = []

    # percorre e2 da direita para a esquerda
    for i, dig in enumerate(reversed(e2)):
        parcial = multiplica_um_digito(e1, dig, base)
        
        # adiciona zeros conforme a posição
        parcial += '0' * i
    
        resultados.append(parcial)

    # soma todas as partes
    resultado_final = '0'
    
    for termo in resultados:
        resultado_final = soma_em_base_n(resultado_final, termo, base)

    return resultado_final

# converte de uma base A para a base B
def converte_bases(numero1: str, base_origem: int , base_destino: int):
    simbolos = '0123456789ABCDEFGHIJKLMNOP'
    
    maior_base, menor_base = max(base_origem, base_destino), min(base_origem, base_destino)
    algarismo_maior = simbolos[:maior_base]
    
    # dicionario de equivalências: base maior em base menor
    dic_eq = {}
    for i, dig in enumerate(algarismo_maior):
        valor = '0'
        for _ in range(i):
            valor = soma_em_base_n(valor, "1", menor_base)
        dic_eq[dig] = valor
    
    # inverso do dicionario de equivalência: base menor em base maior
    dic_eq_inv = {v: k for k, v in dic_eq.items()}
    
    if base_origem == maior_base:
        resultado = "0"
        
        pot = "1"  # começa com base_origem^0 = 1
        
        # começa com o numero menos significativo
        for dig in reversed(numero1):
            # valor da base maior na base menor
            val = dic_eq[dig]
            
            # multiplica val * pot
            soma = "0"
            
            for _ in range(int(val, menor_base)):
                soma = soma_em_base_n(soma, pot, menor_base)
            
            # acumula no resultado
            resultado = soma_em_base_n(resultado, soma, menor_base)
            
            # atualiza potência (pot *= base_origem)
            nova_pot = "0"
            for _ in range(base_origem):
                nova_pot = soma_em_base_n(nova_pot, pot, menor_base)
            pot = nova_pot
        
        print(f"{numero1} (base {base_origem}) = {resultado} (base {base_destino})")
        return resultado
    
    else:
        # o número está escrito em base menor
        acumulado = numero1
        resultado = ""
        
        while acumulado != "0":
            # acha equivalente no dicionário
            if acumulado in dic_eq_inv:
                resultado = dic_eq_inv[acumulado] + resultado
                break
            
            # se o algarismo não está previsto na tabela -> achar o  dígito da base maior no acumulado 
            for simbolo, val in reversed(dic_eq.items()):
                if int(val, menor_base) <= int(acumulado, menor_base):
                    resultado = simbolo + resultado
                    acumulado = format(int(acumulado, menor_base) - int(val, menor_base), f"{menor_base}")
                    break
        
        print(f"{numero1} (base {base_origem}) = {resultado} (base {base_destino})")
        # return resultado
