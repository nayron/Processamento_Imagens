# -*- coding: utf-8 -*-
# Projeto 9 - Processamento de imagens

from __future__ import print_function
from __future__ import division

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

def cria_histograma(imagem):
    """Cria o histograma da imagem"""
    r = 0; n = 1; pr = 2
    
    lista = range(256)
    for i in range(256):
        # número de tons de cinza; frequência
        lista[i] = [i, 0, 0.0]
    
    # Define o número de tons de cinza na imagem
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            lista[imagem[i, j]][n] += 1
    
    # Define a frequência com que os tons de cinza aparecem
    for i in range(len(lista)):
        lista[i][pr] = float(lista[i][n] / (imagem.shape[0] * imagem.shape[1]))
    
    return lista
    
def vale(imagem):
    """Acha o valor do thresholding"""
    r = 0; n = 1; pr = 2
    lista = cria_histograma(imagem)
    
    # Acha o primeiro vale do meio para frente
    for i in range(128, len(lista)):
        if lista[i + 1][pr] > lista[i][pr]:
            frente = lista[i + 1][r]
            break
    
    # Acha o primeiro vale do meio para trás
    for i in range(128, 0, -1):
        if lista[i - 1][pr] > lista[i][pr]:
            tras = lista[i + 1][r]
            break
    
    # Define o mais próximo do meio do histograma
    if frente < tras:
        return frente
    return tras

def segmenta(imagem):
    """Segmenta a imagem utilizando o método do vale como limiar"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    valor = vale(imagem)
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if imagem[i, j] < valor:
                nova_imagem[i, j] = 0
            else:
                nova_imagem[i, j] = 255
    
    return nova_imagem

imagem = cv.imread('../Imagens/lena.bmp', cv.IMREAD_GRAYSCALE)
imprime_imagem('Imagem original', imagem)

imagem = segmenta(imagem)
imprime_imagem('Imagem segmentada', imagem)
