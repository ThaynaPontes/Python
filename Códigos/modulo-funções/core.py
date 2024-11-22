def somaLista (valores=[]):

    """
    A função somaLista, recebe uma lista de números e faz uma soma de todos os números da lista e retorna o resultado da soma

    Parameters
-----------------------
    Valores: int[]
    Lista de números para a soma

    Returns
-----------------------
    Retorna a soma de uma lista
"""

    resultado = 0
    for i in valores:
        resultados+=i

    return resultado

def Maiorvalor(lista=[]):
    """
    A função maiorValor encontra o maior valor em uma lista númerica.
    
    Parameters
    -------------------------
        lista: int[]

    Returns
    -------------------------
        Retorna o maior valor da lista
    """

    m = lista[0]
    for i in lista:
        if i > m:
            m = i

    return m

def inverter(palavra=""):
    # Vamos utilizar o comando len(length - comprimento) para obter a quantidade de caracteres da palavra.
    qtd =  len(palavra)
    invertida = ""