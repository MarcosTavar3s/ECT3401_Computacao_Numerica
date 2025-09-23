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


def converte(numero1: str, base_origem: int, base_destino: int):
    n_aux = '0'
    n_destino = '0'
    
    while n_aux != numero1:
        n_aux = soma_em_base_n(n_aux, '1', base_origem)
        n_destino = soma_em_base_n(n_destino, '1', base_destino)
        
        print(f'Numero na base {base_origem}: {n_aux}, Numero na base {base_destino}:{n_destino}')

    print(n_destino)
    
