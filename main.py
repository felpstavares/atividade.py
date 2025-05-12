def analisar_numeros(numeros):
    """
    Função que analisa uma lista de números inteiros e retorna algumas estatísticas.
    
    Parâmetros:
    numeros (list): Lista de números inteiros.
    
    Retorna:
    dict: Dicionário com a média, maior número, menor número e quantidade de números pares.
    """
    if not numeros:
        return {
            "media": 0,
            "maior": 0,
            "menor": 0,
            "pares": 0
        }
    
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    pares = len([num for num in numeros if num % 2 == 0])
    
    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "pares": pares
    }

