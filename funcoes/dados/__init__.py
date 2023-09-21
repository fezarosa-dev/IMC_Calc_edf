import openpyxl
import json


def makexlsx(file_name):
    # Read the JSON file
    with open('people.json', 'r') as json_file:
        json_data = json.load(json_file)

    # Create a new XLSX file
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Check if there is data in the JSON
    if json_data:
        # Add a header with the keys from the first dictionary in the JSON as column names
        header = list(json_data[0].keys())
        sheet.append(header)

        # Add JSON data to the spreadsheet
        for row in json_data:
            data = list(row.values())
            sheet.append(data)

        # Save the spreadsheet to an XLSX file
        workbook.save(file_name)

        print("Planilha criada com sucesso.")
    else:
        print("O JSON está vazio. Não foi criada nenhuma planilha.")


import os
def verificar_e_corrigir_json(nome_arquivo):
    with open(nome_arquivo, 'rb+') as arquivo:
        # Leitura do primeiro caractere
        primeiro_caractere = arquivo.read(1)

        # Se o primeiro caractere não for '[', adicione '[' no início do arquivo
        if primeiro_caractere != b'[':
            arquivo.seek(0)
            conteudo_resto = arquivo.read()
            arquivo.seek(0)
            arquivo.write(b'[' + conteudo_resto)

        # Desloque o cursor para o final do arquivo
        arquivo.seek(-1, os.SEEK_END)
        # Leitura do último caractere
        ultimo_caractere = arquivo.read(1)

        # Se o último caractere não for ']', adicione ']' no final do arquivo
        if ultimo_caractere != b']':
            arquivo.seek(-1, os.SEEK_END)
            arquivo.write(b']')


