def ler_eleitores(caminho_arquivo):
    eleitores = []
    
# Abre o arquivo em modo de leitura
    with open(caminho_arquivo, 'r') as file:
        # Lê cada linha do arquivo
        for linha in file:
            # Divide a linha usando a vírgula como separador
            elementos = linha.strip().split(", ")
            
            # Adiciona os elementos ao mapa ou matriz
            info = {
                'nome': elementos[0],
                'rg': elementos[1],
                'titulo': elementos[2],
                'cidade': elementos[3],
                'estado': elementos[4],
            }
            eleitores.append(info)
        return eleitores