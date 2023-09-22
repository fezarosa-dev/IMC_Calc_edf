import json
import logging
import math
import tkinter as tk
import tkinter.simpledialog as simpledialog
import openpyxl
import os
# Função para criar uma planilha XLSX com base nos dados do JSON


class Estilos:
    """
    Define códigos de estilo para aplicar em texto no terminal.
    """
    RESET = '\033[0m'  # Reseta todos os estilos e cores
    BOLD = '\033[1m'   # Torna o texto em negrito
    ITALIC = '\033[3m'  # Torna o texto em itálico
    UNDERLINE = '\033[4m'  # Sublinha o texto

class Cores:
    """
    Define códigos de cores para aplicar em texto no terminal.
    """
    RESET = '\033[0m'  # Reseta todas as cores

    # Cores básicas
    preto = '\033[30m'  # Texto preto
    vermelho = '\033[31m'  # Texto vermelho
    verde = '\033[32m'  # Texto verde
    amarelo = '\033[33m'  # Texto amarelo
    azul = '\033[34m'  # Texto azul
    magenta = '\033[35m'  # Texto magenta
    ciano = '\033[36m'  # Texto ciano
    branco = '\033[37m'  # Texto branco
    laranja = '\033[38;5;202m'  # Texto laranja
    rosa = '\033[38;5;206m'  # Texto rosa

    # Cores adicionais
    roxo = '\033[38;5;92m'  # Texto roxo
    turquesa = '\033[38;5;45m'  # Texto turquesa
    dourado = '\033[38;5;178m'  # Texto dourado
    verde_claro = '\033[38;5;120m'  # Texto verde claro
    cinza_claro = '\033[38;5;250m'  # Texto cinza claro
    cinza_escuro = '\033[38;5;240m'  # Texto cinza escuro
    marrom = '\033[38;5;130m'  # Texto marrom

def texto_estilizado(texto, estilo):
    return f"{estilo}{texto}{Estilos.RESET}"

def imprimir_texto_estilizado(texto, estilo):
    estilizado = texto_estilizado(texto, estilo)
    print(estilizado)

def titulo(texto=None, estilo=None, aplicar_cores="ambos"):
    """
    Imprime uma mensagem centralizada, enquadrada por linhas de traços.

    Essa função aceita um texto para título e o imprime centralizado
    entre linhas de traços, criando um quadro estético.

    :param texto: O texto para exibir no centro das linhas de traços.
                 Se for None, a função não fará nada.
    :type texto: str ou None
    :param estilo: O código de estilo a ser aplicado ao texto do título.
                   Padrão: None
    :type estilo: str ou None
    :param aplicar_cores: Determina onde aplicar as cores e estilos.
                          "ambos" (padrão) - Aplica a cor/estilo tanto ao texto quanto às linhas.
                          "texto" - Aplica a cor/estilo somente ao texto.
                          "linhas" - Aplica a cor/estilo somente às linhas.
    :type aplicar_cores: str

    Exemplo de uso:
    ---------------
    >>> titulo("Exemplo", Cores.vermelho, aplicar_cores="texto")
    ------------------------------
              Exemplo
    ------------------------------
    """
    if texto is None:
        return
    else:
        texto = str(texto)
        if len(texto) * 2 < 30:
            linha = "-" * 30
            mensagem = f"{texto:^30}"
        else:
            linha = "-" * (len(texto) * 2)
            mensagem = f"{texto:^{len(texto) * 2}}"

        if estilo:
            if aplicar_cores == "ambos":
                imprimir_texto_estilizado(linha, estilo)
                imprimir_texto_estilizado(mensagem, estilo)
                imprimir_texto_estilizado(linha, estilo)
            elif aplicar_cores == "texto":
                imprimir_texto_estilizado(linha, Cores.RESET)
                imprimir_texto_estilizado(mensagem, estilo)
                imprimir_texto_estilizado(linha, Cores.RESET)
            elif aplicar_cores == "linha":
                imprimir_texto_estilizado(linha, estilo)
                print(mensagem)
                imprimir_texto_estilizado(linha, estilo)
            else:
                imprimir_texto_estilizado(linha, estilo)
                imprimir_texto_estilizado(mensagem, estilo)
                imprimir_texto_estilizado(linha, estilo)
        else:
            print(linha)
            print(mensagem)
            print(linha)

def makexlsx(file_name):
    verificar_e_corrigir_json('people.json')
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
    root.quit()
    # Nome do arquivo JSON
    file_name_json = 'people.json'

    counter = 1

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

        # Abrir o arquivo JSON em modo de leitura (para verificar a estrutura)
        with open(file_name_json, 'r') as arquivo_json:
            try:
                # Tentar carregar a lista de dados existente no arquivo
                dados = json.load(arquivo_json)
            except json.JSONDecodeError:
                # Se o arquivo estiver vazio ou mal formatado, criar uma lista vazia
                dados = []

        # Adicionar o novo dicionário à lista de dados
        dados.append(informations_dict)

        # Abrir o arquivo JSON em modo de escrita e escrever a lista atualizada de dados
        with open(file_name_json, 'w') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)

        titulo(f"{informations_dict['name']} número: {counter}, tem o IMC de {informations_dict['imc']}, sendo {informations_dict['imcStatus']}" , Cores.roxo)
        stop = input('Deseja parar? (S para parar): ')
        if stop.lower() == 's':
            break

        counter += 1

    # Registrar o número total de registros no arquivo de log
    logging.basicConfig(filename='quantity.log', level=logging.INFO, format='%(message)s', filemode='w')
    logging.info(counter)

# Função para gerar planilhas com os dados existentes
def gerar_planilhas():
    root.quit()
    # Solicitar o nome do arquivo XLSX
    file_name_xlsx = simpledialog.askstring("Nome do Arquivo XLSX", "Digite o nome do arquivo XLSX:")
    file_name_xlsx = file_name_xlsx.strip()

    if not file_name_xlsx.endswith('.xlsx'):
        file_name_xlsx += '.xlsx'
    makexlsx(file_name_xlsx)

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
