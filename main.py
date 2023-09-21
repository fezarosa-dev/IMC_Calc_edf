import json
import logging
import math
import tkinter as tk
import tkinter.simpledialog as simpledialog
import openpyxl
import os
from funcoes import terminal
# Função para criar uma planilha XLSX com base nos dados do JSON
def makexlsx(file_name):
    # Ler o arquivo JSON
    with open('people.json', 'r') as json_file:
        json_data = json.load(json_file)

    # Criar uma nova planilha XLSX
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Verificar se há dados no JSON
    if json_data:
        # Adicionar um cabeçalho com os nomes das colunas com base nas chaves do primeiro dicionário no JSON
        header = list(json_data[0].keys())
        sheet.append(header)

        # Adicionar os dados do JSON à planilha
        for row in json_data:
            data = list(row.values())
            sheet.append(data)

        # Salvar a planilha em um arquivo XLSX
        workbook.save(file_name)

        print("Planilha criada com sucesso.")
    else:
        print("O JSON está vazio. Nenhuma planilha foi criada.")

# Função para verificar e corrigir o formato do JSON
def verificar_e_corrigir_json(nome_arquivo):
    with open(nome_arquivo, 'rb+') as arquivo:
        # Ler o primeiro caractere
        primeiro_caractere = arquivo.read(1)

        # Se o primeiro caractere não for '[', adicione '[' no início do arquivo
        if primeiro_caractere != b'[':
            arquivo.seek(0)
            conteudo_resto = arquivo.read()
            arquivo.seek(0)
            arquivo.write(b'[' + conteudo_resto)

        # Deslocar o cursor para o final do arquivo
        arquivo.seek(-1, os.SEEK_END)
        # Ler o último caractere
        ultimo_caractere = arquivo.read(1)

        # Se o último caractere não for ']', adicione ']' no final do arquivo
        if ultimo_caractere != b']':
            arquivo.seek(-1, os.SEEK_END)
            arquivo.write(b']')

# Função para coletar dados das pessoas e salvar em JSON
def coletar_dados():
    # Nome do arquivo JSON
    file_name_json = 'people.json'

    counter = 1

    if not os.path.isfile(file_name_json):
        # Crie um dicionário vazio
        dados = []

        # Crie o arquivo JSON em branco
        with open(file_name_json, 'w') as arquivo:
            json.dump(dados, arquivo)

    while True:
        informations_dict = {}

        while True:
            name = input('Digite o nome: ')
            if name.replace(' ', '').isalpha():
                break

        while True:
            age = input('Digite a idade: ')
            if age.isdigit():
                age = float(age)
                break

        while True:
            gender = input('Digite o gênero (M para masculino e F para feminino): ')
            if gender.isalpha() and gender.lower() in 'mf':
                gender = gender.lower()
                break

        while True:
            weight = input('Digite o peso: ')
            if weight.replace(',', '', 1).replace('.', '', 1).isdigit():
                weight = float(weight.replace(',', '.', 1))
                break

        while True:
            height = input('Digite a altura (use ponto para separar decimais, por exemplo, 1.75): ')
            if height.replace(',', '', 1).replace('.', '', 1).replace(' ', '').replace('m', '').isdigit():
                height = float(height.replace(',', '.', 1).replace('m', ''))
                if height > 3:
                    height = height / 100
                break
        imc = weight / math.pow(height, 2)

        if imc < 18.5:
            imcstatus = "Abaixo do peso"
        elif 18.5 <= imc < 25.0:
            imcstatus = "Peso saudável"
        elif 25.0 <= imc < 30.0:
            imcstatus = "Sobrepeso"
        elif 30.0 <= imc < 35.0:
            imcstatus = "Obesidade grau 1"
        elif 35.0 <= imc < 40.0:
            imcstatus = "Obesidade grau 2"
        else:
            imcstatus = "Obesidade grau 3 (obesidade morbida)"
        informations_dict = {
            'name': name,
            'age': age,
            'gender': gender,
            'weight': weight,
            'height': height,
            'imc': imc,
            'imcStatus': imcstatus,
        }

        with open(file_name_json, 'a') as arquivo_json:
            # Verifica se o arquivo não está vazio (se já possui pelo menos um dicionário)
            arquivo_json.seek(0, 2)  # Move o cursor para o final do arquivo
            if arquivo_json.tell() > 0:
                arquivo_json.write(',')  # Adiciona uma vírgula antes do novo dicionário

            # Adiciona o novo dicionário à lista no arquivo JSON
            json.dump(informations_dict, arquivo_json, indent=4)

        print(f"{informations_dict['name']} número: {counter}, tem o IMC de {informations_dict['imc']}, sendo {informations_dict['imcStatus']}")
        stop = input('Deseja parar? (S para parar): ')
        if stop.lower() == 's':
            break

        counter += 1

    # Registrar o número total de registros no arquivo de log
    logging.basicConfig(filename='quantity.log', level=logging.INFO, format='%(message)s', filemode='w')
    logging.info(counter)
    verificar_e_corrigir_json(file_name_json)
    root.quit()

# Função para gerar planilhas com os dados existentes
def gerar_planilhas():
    # Solicitar o nome do arquivo XLSX
    file_name_xlsx = simpledialog.askstring("Nome do Arquivo XLSX", "Digite o nome do arquivo XLSX:")
    file_name_xlsx = file_name_xlsx.strip()

    if not file_name_xlsx.endswith('.xlsx'):
        file_name_xlsx += '.xlsx'
    makexlsx(file_name_xlsx)
    root.quit()

# Configurar a interface gráfica usando tkinter
root = tk.Tk()
root.title("Selecione uma Opção")

label = tk.Label(root, text="Escolha uma opção:")
label.pack()

pegar_button = tk.Button(root, text="Pegar Dados", command=coletar_dados)
pegar_button.pack()

gerar_button = tk.Button(root, text="Gerar Planilhas com Dados Existentes", command=gerar_planilhas)
gerar_button.pack()

root.mainloop()
