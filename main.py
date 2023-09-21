import tkinter as tk
import tkinter.simpledialog as simpledialog
from funcoes import dados
from funcoes import terminal
from time import sleep
import logging

# Solicitar o nome do arquivo
file_name = simpledialog.askstring("Nome do Arquivo", "Digite o nome do arquivo:")
file_name.strip()
if file_name[-4:] != 'xlsx':
    file_name = file_name + '.xlsx'

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

    informations_dict = {
        'name': name,
        'age': age,
        'gender': gender,
        'weight': weight,
        'height': height,
    }

    stop = input('Deseja parar? (S para parar): ')
    if stop.lower() == 's':
        break

    counter += 1

logging.basicConfig(filename='quantity.log', level=logging.INFO, format='%(message)s')
logging.info(counter)
print(informations_dict)
