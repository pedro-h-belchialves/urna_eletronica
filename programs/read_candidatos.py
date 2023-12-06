def ler_candidatos(caminho_arquivo):
    candidatos = []
    
# Abre o arquivo em modo de leitura
    with open(caminho_arquivo, 'r') as file:
        # Lê cada linha do arquivo
        for linha in file:
            # Divide a linha usando a vírgula como separador
            elementos = linha.strip().split(", ")
            
            # Adiciona os elementos ao mapa ou matriz
            info = {
                'nome': elementos[0],
                'numero': elementos[1],
                'partido': elementos[2],
                'estado': elementos[3],
                'cargo': elementos[4],
            }
            candidatos.append(info)
        return candidatos