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
