# -*- coding: utf-8 -*-
# Projeto 7 - Processamento de imagens
##Náyron dos Anjos, Bruno Vinicios de Sá

from __future__ import print_function
from __future__ import division

import cv2 as cv
import numpy as np

# as quatro máscaras que serão utilizadas
quatro_negativo = [0, 1, 0], [1, -4, 1], [0, 1, 0]
quatro_positivo = [0, -1, 0], [-1, 4, -1], [0, -1, 0]
oito_negativo = [1, 1, 1], [1, -8, 1], [1, 1, 1]
oito_positivo = [-1, -1, -1], [-1, 8, -1], [-1, -1, -1]

def imprime_imagem(tipo, imagem):
    """Monta a imagem novamente e imprime"""
    cv.imshow(tipo, imagem)
    cv.waitKey(0)
    cv.destroyAllWindows()

def cria_nova_imagem(altura, largura):
    """Cria uma nova imagem vazia com base nas dimensões passadas"""
    imagem = np.empty((altura, largura, 3), np.uint8)
    imagem[:] = 255
    return imagem

def laplaciano(imagem, mascara):
    """Executa a filtragem laplaciana na imagem"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            nova_imagem[i, j] = calcula_valor(imagem, mascara, i, j)
    
    return nova_imagem

def calcula_valor(imagem, mascara, x, y):
    """Define os valores de pixel que serão utilizados no cálculo"""
    valores = []
    mi = -1
    
    for i in range(x - 1, x + 2):
        mi += 1; mj = 0
        for j in range(y - 1, y + 2):
            if i < 0 or j < 0 or i >= imagem.shape[0] or j >= imagem.shape[1]:
                continue
            valores.append(imagem[i, j] * mascara[mi][mj])
            mj += 1
    
    valor = 0
    for i in range(len(valores)):
        valor += valores[i]
    valor /= 9
    valor +=255
    if valor < 0:
        return 0
    return valor

imagem = cv.imread('../Imagens/lena.bmp', cv.IMREAD_GRAYSCALE)
imprime_imagem('Original', imagem)

nova_imagem = laplaciano(imagem, quatro_negativo)
print('Máscara com o 4 negativo no centro')
imprime_imagem('Máscara com o 4 negativo no centro', nova_imagem)

nova_imagem = laplaciano(imagem, quatro_positivo)
print('Máscara com o 4 positivo no centro')
imprime_imagem('Máscara com o 4 positivo no centro', nova_imagem)

nova_imagem = laplaciano(imagem, oito_negativo)
print('Máscara com o 8 negativo no centro')
imprime_imagem('Máscara com o 8 negativo no centro', nova_imagem)

nova_imagem = laplaciano(imagem, oito_positivo)
print('Máscara com o 8 positivo no centro')
imprime_imagem('Máscara com o 8 positivo no centro', nova_imagem)
