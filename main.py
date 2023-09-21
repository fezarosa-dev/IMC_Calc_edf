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
informations_list = []

while True:
    while True:
        name = input('Digite o nome: ')
        if name.isalpha():
            break
    while True:
        age = input('Digite a idade: ')
        if age.isdigit():
            age = float(age)
            break
    while True:
        gender = input('Digite o genero (M para masculino e F para feminino): ')
        if gender.isalpha():
            if gender.lower() in 'mf':
                gender = gender.lower()
                break
    while True:
        weight = input('Digite o peso: ')
        if weight.isdigit():
            altura = float(altura)
            if float(altura) >= 3:
                altura = float(altura)
            break
    height = input('Digite a altura: ')

    stop = input('Deseja parar? (S para parar): ')
    if stop.lower() =='s':
        break


    informations = {
        'name': name,
        'age': age,
        'gender': gender,
        'weight': weight,
        'height': height,
        }


    counter += 1

logging.basicConfig(filename='meu_numero.log', level=logging.INFO, format='%(message)s')
logging.info(counter)
