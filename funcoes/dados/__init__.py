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
