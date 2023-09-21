# Documentação do Código

Este documento fornece uma explicação detalhada do código Python fornecido. O código em questão realiza várias operações relacionadas à coleta e manipulação de dados pessoais, bem como à criação de planilhas XLSX a partir desses dados usando a biblioteca `openpyxl` e uma interface gráfica simples com o módulo `tkinter`. A documentação a seguir abordará cada parte do código e suas funcionalidades.

## Importação de Bibliotecas

```python
import json 
import logging 
import math 
import tkinter as tk 
import tkinter.simpledialog as simpledialog 
import openpyxl 
import os 
from funcoes import terminal
```

- `json`: Biblioteca para lidar com operações JSON.
- `logging`: Biblioteca para fazer log de informações.
- `math`: Biblioteca para cálculos matemáticos (usada para cálculos IMC).
- `tkinter`: Biblioteca para criar a interface gráfica.
- `tkinter.simpledialog`: Módulo para caixas de diálogo simples.
- `openpyxl`: Biblioteca para criar e manipular planilhas XLSX.
- `os`: Biblioteca para operações de sistema.
- `funcoes`: Importa funções do módulo `funcoes`.

## Função `makexlsx(file_name)`

```python
def makexlsx(file_name):
    # ...
```

- Esta função cria uma planilha XLSX com base nos dados de um arquivo JSON fornecido como entrada.
- Lê o arquivo JSON chamado `people.json` e carrega seus dados em uma lista.
- Cria uma nova planilha XLSX, adiciona um cabeçalho com base nas chaves do primeiro dicionário no JSON e, em seguida, adiciona os dados do JSON à planilha.
- Finalmente, salva a planilha no arquivo especificado (`file_name`).

## Função `verificar_e_corrigir_json(nome_arquivo)`

```python
def verificar_e_corrigir_json(nome_arquivo):
    # ...
```

- Esta função verifica e corrige o formato de um arquivo JSON.
- Abre o arquivo em modo binário (`'rb+'`) e verifica se o primeiro caractere é `[`. Se não for, adiciona `[` no início do arquivo.
- Desloca o cursor para o final do arquivo e verifica se o último caractere é `]`. Se não for, adiciona `]` no final do arquivo.

## Função `coletar_dados()`

```python
def coletar_dados():
    # ...
```

- Esta função permite que o usuário colete informações pessoais, calcule o IMC (Índice de Massa Corporal) com base nos dados inseridos e salve essas informações em um arquivo JSON chamado `people.json`.
- Solicita ao usuário que insira o nome, idade, gênero, peso e altura.
- Calcula o IMC com base nos valores de peso e altura.
- Determina a categoria IMC (Abaixo do peso, Peso saudável, Sobrepeso, etc.).
- Registra os dados no arquivo JSON, adicionando-os à lista existente, se houver.
- Exibe informações sobre a pessoa coletada e permite ao usuário continuar ou parar a coleta.
- Registra o número total de registros no arquivo de log `quantity.log`.
- Chama a função `verificar_e_corrigir_json` para garantir que o arquivo JSON tenha o formato correto.

## Função `gerar_planilhas()`

```python
def gerar_planilhas():
    # ...
```

- Esta função cria uma planilha XLSX a partir dos dados existentes no arquivo JSON `people.json`.
- Solicita ao usuário que insira o nome do arquivo XLSX que deseja criar.
- Chama a função `makexlsx` para criar a planilha e salva-a com o nome fornecido.

## Configuração da Interface Gráfica

```python
root = tk.Tk()
root.title("Selecione uma Opção")

label = tk.Label(root, text="Escolha uma opção:")
label.pack()

pegar_button = tk.Button(root, text="Pegar Dados", command=coletar_dados)
pegar_button.pack()

gerar_button = tk.Button(root, text="Gerar Planilhas com Dados Existentes", command=gerar_planilhas)
gerar_button.pack()

root.mainloop()
```

- Essa parte do código configura a interface gráfica usando a biblioteca `tkinter`.
- Cria uma janela principal (`root`) com um título.
- Adiciona um rótulo e dois botões à janela.
- O botão "Pegar Dados" chama a função `coletar_dados` quando pressionado.
- O botão "Gerar Planilhas com Dados Existentes" chama a função `gerar_planilhas` quando pressionado.
- A interface gráfica permanece ativa até que o usuário a feche.