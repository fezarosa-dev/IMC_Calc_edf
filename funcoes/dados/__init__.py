from openpyxl import Workbook


def criar_arquivo_xlsx_com_colunas(nome_arquivo, nomes_colunas):
    try:
        workbook = Workbook()
        sheet = workbook.active

        # Inserir os nomes das colunas na primeira linha da planilha
        for idx, nome_coluna in enumerate(nomes_colunas, start=1):
            sheet.cell(row=1, column=idx, value=nome_coluna)

        # Salvar o arquivo XLSX
        workbook.save(nome_arquivo)

        print(f"Arquivo '{nome_arquivo}' criado com sucesso com as colunas: {', '.join(nomes_colunas)}")
    except Exception as e:
        print(f"Erro ao criar o arquivo XLSX: {str(e)}")
