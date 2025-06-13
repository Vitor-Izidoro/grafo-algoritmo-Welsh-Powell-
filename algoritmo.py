def welsh_powell_coloring(grafo):
    # Ordena os estados por grau (número de vizinhos), decrescente
    vertices_ordenados = sorted(grafo, key=lambda x: len(grafo[x]), reverse=True)

    coloracao = {}
    cor = 0
    cores_usadas = []

    for vertice in vertices_ordenados:
        if vertice not in coloracao:
            cor += 1
            coloracao[vertice] = cor
            for outro_vertice in vertices_ordenados:
                if outro_vertice not in coloracao:
                    # Verifica se pode receber essa cor
                    if all(coloracao.get(vizinho) != cor for vizinho in grafo[outro_vertice]):
                        coloracao[outro_vertice] = cor

    # Transforma o dicionário em lista de tuplas
    return list(coloracao.items())

# Grafo do Brasil
grafo_brasil = {
    "AC": ["AM", "RO"],
    "AL": ["BA", "PE", "SE"],
    "AP": ["PA"],
    "AM": ["AC", "RR", "PA", "MT", "RO"],
    "BA": ["AL", "SE", "PE", "PI", "GO", "MG", "ES"],
    "CE": ["PI", "PE", "PB", "RN"],
    "DF": ["GO", "MG"],
    "ES": ["BA", "MG", "RJ"],
    "GO": ["MT", "MS", "MG", "DF", "BA", "TO"],
    "MA": ["PA", "TO", "PI"],
    "MT": ["RO", "AM", "PA", "TO", "GO", "MS"],
    "MS": ["MT", "GO", "MG", "SP", "PR"],
    "MG": ["BA", "GO", "DF", "MS", "SP", "RJ", "ES"],
    "PA": ["AP", "AM", "RR", "MA", "TO", "MT"],
    "PB": ["RN", "CE", "PE"],
    "PR": ["SP", "SC", "MS"],
    "PE": ["CE", "PB", "AL", "BA", "PI"],
    "PI": ["MA", "TO", "BA", "PE", "CE"],
    "RJ": ["MG", "ES", "SP"],
    "RN": ["CE", "PB"],
    "RO": ["AC", "AM", "MT"],
    "RR": ["AM", "PA"],
    "RS": ["SC"],
    "SC": ["PR", "RS"],
    "SE": ["AL", "BA"],
    "SP": ["MG", "RJ", "PR", "MS"],
    "TO": ["PA", "MA", "PI", "BA", "GO", "MT"]
}

# Executando o algoritmo
resultado = welsh_powell_coloring(grafo_brasil)

# Exibindo a coloração dos estados
for estado, cor in sorted(resultado):
    print(f"{estado}: Cor {cor}")
