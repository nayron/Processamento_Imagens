# -*- coding: utf-8 -*-
# Projeto 1 - Processamento de imagens

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def imprime_imagem(tipo, imagem):
    """Monta a imagem novamente e imprime"""
    cv.imshow(tipo, imagem)
    cv.waitKey(0)
    cv.destroyAllWindows()

def cria_nova_imagem(altura, largura):
    """Cria uma nova imagem vazia com base nas dimensões passadas"""
    return np.zeros((altura, largura, 3), np.uint8)

def vizinho_reducao(imagem):
    """Reduz a imagem usando interpolação por vizinho mais próximo"""
    nova_imagem = cria_nova_imagem(imagem.shape[0] / 2, imagem.shape[1] / 2)
    
    for i in range(nova_imagem.shape[0]):
        for j in range(nova_imagem.shape[1]):
            nova_imagem[i, j] = imagem[i + i, j + j]
    
    return nova_imagem

def bilinear_reducao(imagem):
    """Reduz a imagem usando a interpolação bilinear"""
    nova_imagem = cria_nova_imagem(imagem.shape[0] / 2, imagem.shape[1] / 2)
    
    for i in range(nova_imagem.shape[0]):
        for j in range(nova_imagem.shape[1]):
            r = int(imagem[i + i, j + j][0]) + int(imagem[i + i, j + j + 1][0])
            r += int(imagem[i + i + 1, j + j][0]) + int(imagem[i + i + 1, j + j + 1][0])
            r /= 4
            
            g = int(imagem[i + i, j + j][1]) + int(imagem[i + i, j + j + 1][1])
            g += int(imagem[i + i + 1, j + j][1]) + int(imagem[i + i + 1, j + j + 1][1])
            g /= 4
            
            b = int(imagem[i + i, j + j][2]) + int(imagem[i + i, j + j + 1][2])
            b += int(imagem[i + i + 1, j + j][2]) + int(imagem[i + i + 1, j + j + 1][2])
            b /= 4
            nova_imagem[i, j][0] = r
            nova_imagem[i, j][1] = g
            nova_imagem[i, j][2] = b
             
    return nova_imagem

imagem = cv.imread('lena.bmp')
imprime_imagem('Original', imagem)

# Métodos de redução
nova_imagem = vizinho_reducao(imagem)
imprime_imagem('Redução por vizinho mais próximo', nova_imagem)

nova_imagem = bilinear_reducao(imagem)
imprime_imagem('Redução bilinear', nova_imagem)
