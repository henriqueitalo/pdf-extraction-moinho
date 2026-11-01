import pandas as pd
import os

CABECALHO = [
    "Nº Lab", "Gleba", "Profundidade",
    "pH H2O", "pH KCl", "pH CaCl2",
    "P", "K", "Na", "Ca2+", "Mg2+", "Al3+", "H + Al",
    "SB", "t", "T", "V", "m", "ISNa", "MO", "P-Rem",
    "S", "B", "N", "Cu", "Mn", "Fe", "Zn",
    "Cr", "Ni", "Cd", "Pb",
]

# Quantidade de valores esperada após as tres primeiras colunas
QTD_VALORES = len(CABECALHO) - 3 


def linha_para_lista(id_registro, texto_linha):

    partes = texto_linha.split()

    gleba = partes[1]
    profundidade = partes[2]
    valores = partes[3:]

    # Caso especifico presente  no exemplo, onde o não ha um valor informado.
    if len(valores) == QTD_VALORES - 1:
        valores = valores + ["-"]

    if len(valores) != QTD_VALORES:
        print(
            f"[AVISO] ID {id_registro}: esperado {QTD_VALORES} valores, "
            f"encontrado {len(valores)}. Linha ignorada/verificar manualmente."
        )
        return None

    linha_final = [id_registro, gleba, profundidade] + valores
    return linha_final


def gerar_planilha(dados, caminho_saida):

    os.makedirs("output/", exist_ok=True)

    linhas = []
    for registro in dados:
        for id_registro, texto_linha in registro.items():
            linha = linha_para_lista(id_registro, texto_linha)
            if linha:
                linhas.append(linha)

    df = pd.DataFrame(linhas, columns=CABECALHO)

    df = df.replace("-", pd.NA)

    df.to_excel(caminho_saida, index=False, sheet_name="Planilha1")
    print(f"Planilha gerada: {caminho_saida} ({len(df)} linhas)")
    return df
