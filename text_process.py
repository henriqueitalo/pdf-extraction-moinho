import re
from collections import defaultdict

def process_text_ufv_lab(texto):
    #Pelo ID no inicio da linha o texto inteiro é junto independente da quebra de linha
    padrao = re.compile(r'^\s*(\d{3,})\s*-?\s*(.+)$')

    dados_por_id = defaultdict(list)

    for linha in texto.splitlines():
        linha = linha.strip()
        if not linha:
            continue

        match = padrao.match(linha)
        if match:
            id_registro = match.group(1)
            resto_da_linha = match.group(2).strip()
            dados_por_id[id_registro].append(resto_da_linha)

    resultado = []
    for id_registro, partes in dados_por_id.items():
        aux = {}
        aux[id_registro] = " ".join(partes)
        resultado.append(aux)

    return resultado


def process_text(texto):
    if 'Universidade Federal de Viçosa' in texto:
        return process_text_ufv_lab(texto)
    else:
        pass
