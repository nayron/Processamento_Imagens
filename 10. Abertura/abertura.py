# -*- coding: utf-8 -*-
# Projeto 9 - Processamento de imagens

from __future__ import print_function

import cv2 as cv
import numpy as np

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

def quantiza(imagem):
    """Executa o algoritmo de quantização na imagem"""
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if imagem[i, j] < 127:
                imagem[i, j] = 0
            else:
                imagem[i, j] = 255
    return imagem

def erosao(imagem):
    """Realiza a operação de erosão na imagem"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0] - 2):
        for j in range(imagem.shape[1] - 2):
            if not precisa_erodir(imagem, i, j):
                nova_imagem[i, j] = 0

    # print(nova_imagem)
    
    return nova_imagem

def precisa_erodir(imagem, i, j):
    """Checa se é necessário remover o pixel no método da erosão"""
    if imagem[i, j] == 0 and \
        imagem[i - 1, j] == 0 and \
        imagem[i, j - 1] == 0 and \
        imagem[i, j + 1] == 0 and \
        imagem[i + 1, j] == 0:
        return False
    return True

def dilatacao(imagem):
    """Realiza a operação de dilatação na imagem"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0] - 2):
        for j in range(imagem.shape[1] - 2):
            if precisa_dilatar(imagem, i, j):
                nova_imagem[i - 1, j] = 0
                nova_imagem[i, j - 1] = 0
                nova_imagem[i, j + 1] = 0
                nova_imagem[i + 1, j] = 0
    
    return nova_imagem

def precisa_dilatar(image, i, j):
    """Checa se é possível dilatar o pixel no método da dilatação"""
    if imagem[i, j] == 0:
        return True
    return False
    
def abertura(imagem):
    """Aplica o método da abertura na imagem"""
    imagem = erosao(imagem)
    imprime_imagem('Imagem erodida', imagem)
    imagem = dilatacao(imagem)
    imprime_imagem('Imagem dilatada', imagem)
    return imagem

imagem = cv.imread('../Imagens/lena.bmp', cv.IMREAD_GRAYSCALE)
imprime_imagem('Imagem original', imagem)

imagem = quantiza(imagem)
imprime_imagem('Imagem binarizada', imagem)

imagem = abertura(imagem)
