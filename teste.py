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
verificar_e_corrigir_json('people.json')
