def char_valor(c: str) -> int:
    if c.isdigit():
        return int(c)
    return ord(c.upper()) - ord('A') + 10

def valor_char(n: int) -> str:
    if n < 10:
        return str(n)
    return chr(ord('A') + n - 10)

def soma_em_base_n(e1: str, e2: str, base: int) -> str:
    e1 = e1.upper()
    e2 = e2.upper()

    # separa as partes 
    if '.' in e1: 
        parte_int1, parte_frac1 = e1.split('.')
    else:
        parte_int1, parte_frac1 = e1, ''
    
    if '.' in e2:
        parte_int2, parte_frac2 = e2.split('.')
    else:
        parte_int2, parte_frac2 = e2, ''

    # padroniza tamanho das partes
    max_frac = max(len(parte_frac1), len(parte_frac2))
    
    # parte e preenchido com zeros para a operacao dar certo
    parte_frac1 = parte_frac1.ljust(max_frac, '0')
    parte_frac2 = parte_frac2.ljust(max_frac, '0')

    # soma parte fracionária
    resultado_frac = []
    
    # lembrei de circuitos digitais
    cin = 0
    
    for i in range(max_frac - 1, -1, -1):
        s = char_valor(parte_frac1[i]) + char_valor(parte_frac2[i]) + cin
        cin = s // base
        resultado_frac.append(valor_char(s % base))
    resultado_frac = ''.join(resultado_frac[::-1])


    # soma parte inteira
    parte_int1 = list(parte_int1.zfill(max(len(parte_int1), len(parte_int2))))
    parte_int2 = list(parte_int2.zfill(max(len(parte_int1), len(parte_int2))))

    resultado_int = []
    for i in range(len(parte_int1) - 1, -1, -1):
        s = char_valor(parte_int1[i]) + char_valor(parte_int2[i]) + cin
        cin = s // base
        resultado_int.append(valor_char(s % base))

    if cin > 0:
        resultado_int.append(valor_char(cin))

    resultado_int = ''.join(resultado_int[::-1])

    # se tem parte fracionaria, vai juntar tudo
    if max_frac > 0:
        return resultado_int + '.' + resultado_frac
    return resultado_int

# multiplica em uma base qualquer
def multiplica_em_base_n(e1: str, e2: str, base: int) -> str:
    e1 = e1.upper()
    e2 = e2.upper()

    # conta casas decimais
    casas1 = len(e1.split('.')[1]) if '.' in e1 else 0
    casas2 = len(e2.split('.')[1]) if '.' in e2 else 0
    # na multiplicacao a quantidade de casas corresponde a soma dos digitos ou uma unidade a mais
    total_casas = casas1 + casas2

    # troca ponto por um espaco em branco
    e1 = e1.replace('.', '')
    e2 = e2.replace('.', '')

    # multiplicação por somas sucessivas
    resultado = "0"
    
    # inverte porque vai usar as somas
    for i, dig2 in enumerate(e2[::-1]):
        parcial = "0"
        
        for _ in range(char_valor(dig2)):
            parcial = soma_em_base_n(parcial, e1, base)
        
        # deslocar para o numero ficar certo
        if parcial != "0":
            parcial += "0" * i
        resultado = soma_em_base_n(resultado, parcial, base)

    # necessidade de colocar os pontos na multiplicacao
    if total_casas > 0:
        if len(resultado) <= total_casas:
            resultado = "0" * (total_casas - len(resultado) + 1) + resultado
            
        sresultado = resultado[:-total_casas] + "." + resultado[-total_casas:]

    return sresultado.strip('.')

# converte de uma base para a outra
def converte(numero: str, base_origem: int, base_destino: int, precisao: int = 10) -> str:
    # converte de base_origem 
    numero = numero.upper()
    
    if '.' in numero:
        print('abc')
        parte_int, parte_frac = numero.split('.')
    else:
        parte_int, parte_frac = numero, ''

    # parte inteira
    valor = 0
    potencia = 1
    for d in parte_int[::-1]:
        valor += char_valor(d) * potencia
        potencia *= base_origem

    # parte fracionária
    frac_valor = 0
    potencia = base_origem
    for d in parte_frac:
        frac_valor += char_valor(d) / potencia
        potencia *= base_origem

    valor_total = valor + frac_valor

    # converte para base_destino
    parte_int = int(valor_total)
    parte_frac = valor_total - parte_int

    # parte inteira
    if parte_int == 0:
        res_int = "0"
    else:
        res_int = ""
        while parte_int > 0:
            res_int = valor_char(parte_int % base_destino) + res_int
            parte_int //= base_destino

    # parte fracionária
    res_frac = ""
    cont = 0
    while parte_frac > 0 and cont < precisao:
        parte_frac *= base_destino
        digito = int(parte_frac)
        res_frac += valor_char(digito)
        parte_frac -= digito
        cont += 1

    if res_frac:
        return res_int + "." + res_frac
    return res_int


# valida se o numero pertence à base ou não 
# def valida(numero: str, base: int) -> bool:
#     simbolos = "0123456789ABCDEFGHIJKLMNOP"
#     base_simbolos = simbolos[:base]
#     numero = numero.upper().replace('.', '')  # ignora ponto decimal
#     # print(all(c in base_simbolos for c in numero))
#     return all(c in base_simbolos for c in numero)
