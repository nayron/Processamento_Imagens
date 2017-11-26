# -*- coding: utf-8 -*-
# Projeto 5 - Processamento de imagens

from __future__ import print_function
from __future__ import division

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from tabulate import tabulate

n = 0 # Primeira coluna; número de tons de cinza
pr = 1 # Segunda coluna; normalização
freq = 2 # Terceira coluna; cálculo da soma normalizada
eq = 3 # Quarta coluna; look-up table
r = 4 # Quinta coluna; imagem de saída

# Variáveis usadas na geração do gráfico
entrada = range(256); saida = range(256)
for i in range(256):
    entrada[i] = 0
    saida[i] = 0

def imprime_imagem(tipo, imagem):
    """Monta a imagem novamente e imprime"""
    cv.imshow(tipo, imagem)
    cv.waitKey(0)
    cv.destroyAllWindows()

def cria_nova_imagem(altura, largura):
    """Cria uma nova imagem vazia com base nas dimensões passadas"""
    imagem = np.zeros((altura, largura, 3), np.uint8)
    imagem[:] = 255
    return imagem

def monta_histograma(imagem):
    """Executa os passos para a montagem do histograma"""
    lista = inicia_lista()
    tons_totais('entrada', lista, imagem)
    normalizacao(lista)
    soma_normalizada(lista)
    lookup_table(lista)
    arredonda_valores(lista)
    
    return lista

def inicia_lista():
    """Inicia a lista com zeros"""
    lista = range(256)
    for i in range(256):
        # num, normalização, soma normalizada, lut, saída
        lista[i] = [0, 0.0, 0.0, 0.0, 0]
    
    return lista

def tons_totais(tipo, lista, imagem):
    """Calcula o número total de cada tom de cinza na imagem"""
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if tipo == 'entrada':
                lista[imagem[i, j]][n] += 1
                entrada[imagem[i, j]] += 1
            else:
                saida[imagem[i, j][0]] += 1

def normalizacao(lista):
    """Normalização dos valores"""
    for i in range(len(lista)):
        lista[i][pr] = float(lista[i][n] / (imagem.shape[0] * imagem.shape[1]))

def soma_normalizada(lista):
    """Soma normalizada dos valores"""
    for i in range(len(lista)):
        lista[i][freq] = lista[i][pr]
        if i > 0:
            lista[i][freq] += lista[i - 1][freq]

def lookup_table(lista):
    """Cria a look-up table"""
    for i in range(len(lista)):
        lista[i][eq] = lista[i][pr] * 255
        if i > 0:
            lista[i][eq] = lista[i - 1][eq] + (lista[i][pr] * 255)

def arredonda_valores(lista):
    """Arredonda os valores finais para gerar a imagem de saída"""
    for i in range(len(lista)):
        lista[i][r] = int(lista[i][eq])

def gera_imagem_final(imagem, lista):
    """Gera a imagem final com os valores da lista"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
                nova_imagem[i, j] = lista[imagem[i, j]][r]
    
    return nova_imagem

def cria_tabela(lista):
    """Cria uma tabela com os dados do histograma"""
    for i in range(len(lista)):
        lista[i].insert(0, i)
    
    lista.insert(0, ['r(k)', 'n(k)', 'Pr(rk)', 'Freq', 'EQ', 'r(k)'])
    
    print(tabulate(lista))

def cria_grafico(lista):
    """Mostra os tons de cinza da imagem original e a de saída"""
    plt.subplot(2, 1, 1)
    plt.title('Imagem de entrada')
    plt.bar(range(256), entrada, width=0.4, color='green')
    
    plt.subplot(2, 1, 2)
    plt.title('Imagem de saida')
    plt.bar(range(256), saida, width=0.4, color='blue')
    
    plt.tight_layout()
    plt.show()

imagem = cv.imread('../Imagens/lena.bmp', cv.IMREAD_GRAYSCALE)
imprime_imagem("Original", imagem)
lista = monta_histograma(imagem)
cria_tabela(lista)
imagem_saida = gera_imagem_final(imagem, lista)
imprime_imagem("Imagem final", imagem_saida)
lista = tons_totais('saida', lista, imagem_saida)
cria_grafico(lista)
