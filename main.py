from outpdf import processar_pasta
from text_process import process_text
from table_gerenation import gerar_planilha


text, filename = processar_pasta("input/")
processed_text = process_text(text)
gerar_planilha(processed_text, f"output/{filename.replace('.pdf', '.xlsx')}")