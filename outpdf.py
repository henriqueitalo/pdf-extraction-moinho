import glob
import os
import pdfplumber

def processar_pasta(pasta):
    os.makedirs(pasta, exist_ok=True)
    os.makedirs("output/", exist_ok=True)
    arquivos_pdf = glob.glob(os.path.join(pasta, "*.pdf"))

    if not arquivos_pdf:
        print("Nenhum PDF encontrado na pasta.")
        return

    print(f"Encontrados {len(arquivos_pdf)} arquivo(s) PDF.\n")

    for arquivo in arquivos_pdf:
        text = extrair_texto_pdf(arquivo)
        filename = os.path.basename(arquivo)

    return text, filename


def extrair_texto_pdf(caminho_pdf):
    texto_completo = ""

    with pdfplumber.open(caminho_pdf) as pdf:
        for i, pagina in enumerate(pdf.pages):
            texto = pagina.extract_text()
            if texto:
                texto_completo += f"\n--- Página {i + 1} ---\n"
                texto_completo += texto

    return texto_completo

