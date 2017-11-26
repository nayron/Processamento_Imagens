# -*- coding: utf-8 -*-
# Projeto 8 - Processamento de imagens

from __future__ import print_function
from __future__ import division

import cv2 as cv
import numpy as np
import math

# O OpenCV usa o formato BGR em vez do RGB
B = 0; G = 1; R = 2
Y = 0; M = 1; C = 2

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

def cria_nova_tabela(altura, largura):
    """Cria uma nova imagem vazia com base nas dimensões passadas"""
    imagem = np.empty((altura, largura, 3), np.float)
    return imagem

def rgb_para_cmy(imagem):
    """Transforma a imagem RGB em uma imagem CMY"""
    nova_imagem = cria_nova_tabela(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            nova_imagem[i, j][C] = 1 - (imagem[i, j][R] / 255)
            nova_imagem[i, j][M] = 1 - (imagem[i, j][G] / 255)
            nova_imagem[i, j][Y] = 1 - (imagem[i, j][B] / 255)
    
    return nova_imagem

def cmy_para_rgb(imagem):
    """Transforma a imagem CMY em uma imagem RGB"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            nova_imagem[i, j][R] = (1 - imagem[i, j][C]) * 255
            nova_imagem[i, j][G] = (1 - imagem[i, j][M]) * 255
            nova_imagem[i, j][B] = (1 - imagem[i, j][Y]) * 255
    
    return nova_imagem

def rgb_para_yuv(imagem):
    """Transforma a imagem RGB em uma imagem YUV"""
    Y = 0; U = 1; V = 2
    nova_imagem = cria_nova_tabela(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            img_r = imagem[i, j][R]
            img_g = imagem[i, j][G]
            img_b = imagem[i, j][B]
            
            nova_imagem[i, j][Y] =  0.299 * img_r + 0.587 * img_g + 0.114 * img_b
            nova_imagem[i, j][U] = -0.147 * img_r - 0.289 * img_g + 0.436 * img_b
            nova_imagem[i, j][V] =  0.615 * img_r - 0.515 * img_g - 0.100 * img_b
            
    return nova_imagem

def yuv_para_rgb(imagem):
    """Transforma a imagem YUV em uma imagem RGB"""
    Y = 0; U = 1; V = 2
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            img_y = imagem[i, j][Y]
            img_u = imagem[i, j][U]
            img_v = imagem[i, j][V]
            
            nova_imagem[i, j][R] = img_y + 1.140 * img_v
            nova_imagem[i, j][G] = img_y - 0.395 * img_u - 0.581 * img_v
            nova_imagem[i, j][B] = img_y + 2.032 * img_u
    
    return nova_imagem

imagem = cv.imread('../Imagens/lena.bmp')
imprime_imagem('Imagem original (RGB)', imagem)

# nova_imagem = hsi_para_rgb(rgb_para_hsi(imagem))
# imprime_imagem('RGB para HSI e HSI para RGB', nova_imagem)

nova_imagem = cmy_para_rgb(rgb_para_cmy(imagem))
imprime_imagem('RGB para CMY e CMY para RGB', nova_imagem)

nova_imagem = yuv_para_rgb(rgb_para_yuv(imagem))
imprime_imagem('RGB para YUV e YUV para RGB', nova_imagem)
