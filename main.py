import json
import logging
import math
import tkinter as tk
import tkinter.simpledialog as simpledialog

from funcoes import dados
from funcoes import terminal

planilha = bool()


def pegar_dados():
    global planilha
    root.destroy()  # Fecha a janela
    planilha = False


def gerar_planilhas():
    global planilha
    root.destroy()  # Fecha a janela
    planilha = True


root = tk.Tk()
root.title("Selecione uma Opção")

label = tk.Label(root, text="Escolha uma opção:")
label.pack()

pegar_button = tk.Button(root, text="Pegar Dados", command=pegar_dados)
pegar_button.pack()

gerar_button = tk.Button(root, text="Gerar Planilhas com Dados Existentes", command=gerar_planilhas)
gerar_button.pack()

root.mainloop()

if planilha:
    # Solicitar o nome do arquivo
    file_name_xlsx = simpledialog.askstring("Nome do Arquivo XLSX", "Digite o nome do arquivo XLSX:")
    file_name_xlsx.strip()

    if file_name_xlsx[-4:] != 'xlsx':
        file_name_xlsx = file_name_xlsx + '.xlsx'
    dados.makexlsx(file_name_xlsx)

else:
    # Abrir o arquivo XLSX no modo de anexação (não alterar essa parte)
    # ...

    # Nome do arquivo JSON
    file_name_json = 'people.json'

    # Lista para armazenar todas as informações coletadas
    informations_list = []
    counter = 1
    terminal.titulo('Digite tudo que se pede: ', terminal.Cores.roxo)
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
            imcstatus = "Obesidade grau 3 (obesidade mórbida)"
        informations_dict = {
            'name': name,
            'age': age,
            'gender': gender,
            'weight': weight,
            'height': height,
            'imc': imc,
            'imcStatus': imcstatus,
        }

        # Adicionar o dicionário de informações à lista
        informations_list.append(informations_dict)
        terminal.titulo(
        terminal.titulo(f"{informations_dict['name']} numero: {counter}, tem o imc de {informations_dict['imc']}, sendo {informations_dict['imcStatus']}"))
        stop = input('Deseja parar? (S para parar): ')
        if stop.lower() == 's':
            break

        counter += 1

    logging.basicConfig(filename='quantity.log', level=logging.INFO, format='%(message)s', filemode='w')
    logging.info(counter)

    # Salvar a lista de informações em um arquivo JSON
    with open(file_name_json, 'a') as json_file:
        json.dump(informations_list, json_file)
