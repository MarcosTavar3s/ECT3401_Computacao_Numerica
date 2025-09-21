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

# transforma o polinomio de Horner em uma lista de valores
def transforma_polinomio(expressao: str, base_destino: int):
    # separa a expressao em termos: substitui espaços, parentesis e quebra no símbolo de +
    termos = expressao.replace(' ', '').replace('(', '').replace(')', '').split('+')
    
    # pega a base de origem, ou seja, a que é elevada ao expoente, e realiza casting para int
    base_origem = int(termos[0].split('**')[0].split('*')[1])
    
    # para armazenar os cada numero na base de destino
    itens = []
    
    for termo in termos:
        itens.append(exp_para_multiplicacao(termo, base_origem, base_destino))
    
    # depuração p ver se está funcionando
    # print(itens)
    
    # soma todos os valores
    for _ in itens:
        # remove o ultimo item o soma com o anterior
        itens[-1] = soma_em_base_n(itens.pop(), itens[-1] , base_destino)
        
    # a lista passa a ter um unico item ao final, o resultado :)
    return itens[0]
    
# transforma as exponenciais para multiplicacoes na base final
def exp_para_multiplicacao(expressao:str, base_origem: int, base_destino: int):
    numero, expoente = expressao.split('**')
    numero, _ = numero.split('*')
    print(numero, expoente)
    
    # numero = expressao[0]
    # expoente = expressao[-1]
    
    # trocar a base de origem por sua representação na base destino 
    base_origem = soma_em_base_n(str(base_origem), '0', base_destino)        
    
    # trocar o numero por sua representação na base destino
    numero = soma_em_base_n(numero, '0', base_destino)        
        
    # vez = 0 Depuracao
    
    for _ in range(char_valor(expoente)): 
        numero = multiplica_em_base_n(numero, base_origem, base_destino)
        # vez+=1 Depuracao
        
    return numero
    
