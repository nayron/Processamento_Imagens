# -*- coding: utf-8 -*-
# Projeto 7 - Processamento de imagens
#Náyron dos Anjos, Bruno Vinicios de Sá

from __future__ import print_function
from __future__ import division

import cv2 as cv
import numpy as np

mascara_horizontal = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
mascara_vertical = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

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

def gradiente(imagem):
    """Cálcula o aguçamento usando gradiente"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    for i in range(1, imagem.shape[0] - 2):
        for j in range(1, imagem.shape[1] - 2):
            gx = imagem[i+1, j-1] + 2 * imagem[i+1, j] + imagem[i+1, j+1]
            gx -= imagem[i-1, j-1] + 2 * imagem[i-1, j] + imagem[i-1, j+1]
            
            gy = imagem[i-1, j+1] + 2 * imagem[i, j+1] + imagem[i+1, j+1]
            gy -= imagem[i-1, j-1] + 2 * imagem[i, j-1] + imagem[i+1, j-1]
            
            nova_imagem[i, j] = gx
    
    return nova_imagem

imagem = cv.imread('../Imagens/lena128.bmp', cv.IMREAD_GRAYSCALE)
imprime_imagem('Original', imagem)

nova_imagem = gradiente(imagem)
imprime_imagem('Gradiente', nova_imagem)
