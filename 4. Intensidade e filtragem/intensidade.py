# -*- coding: utf-8 -*-
# Projeto 4 - Processamento de imagens

from __future__ import print_function

import cv2 as cv
import numpy as np
import math

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

def transformacao_logaritmica(imagem, c):
    """Executa o algoritmo de transformação logarítmica"""
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            imagem[i, j][0] = c * math.log(1 + imagem[i, j][0])
            imagem[i, j][1] = c * math.log(1 + imagem[i, j][1])
            imagem[i, j][2] = c * math.log(1 + imagem[i, j][2])
    
    return imagem

imagem = cv.imread('../Imagens/lena.bmp')
imprime_imagem('Original', imagem)

nova_imagem = transformacao_logaritmica(imagem, 200)
imprime_imagem('Transformação logarítmica', nova_imagem)
