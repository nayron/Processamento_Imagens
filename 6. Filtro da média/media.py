# -*- coding: utf-8 -*-
# Projeto 6 - Processamento de imagens
#Náyron dos Anjos, Bruno Vinicios de Sá
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

def filtro_media(imagem, mascara, tamanho):
    """Aplica o filtro da média na imagem"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            valor = 0
            
            vizinhanca = define_vizinhanca(imagem, tamanho, i, j)
            for k in range(len(vizinhanca)):
                valor += vizinhanca[k] * mascara
            
            valor = valor / (tamanho * tamanho)
            nova_imagem[i, j] = valor
    
    return nova_imagem

def define_vizinhanca(imagem, tamanho, x, y):
    """Define os valores de pixel que serão utilizados no cálculo"""
    lista = []
    valor = 1
    
    # define o número de pixels que o algoritmo passará se afastando do centro
    for i in range(3, tamanho, 2):
        valor += 1
    
    # adiciona os pixels na lista de vizinhança
    for i in range(x - valor, x + valor + 1):
        for j in range(y - valor, y + valor + 1):
            if i < 0 or j < 0 or i >= imagem.shape[0] or j >= imagem.shape[1]:
                lista.append(0) # padding com zeros
                continue
            lista.append(int(imagem[i, j]))
    
    return lista

imagem = cv.imread('../Imagens/lena.bmp', cv.IMREAD_GRAYSCALE)
imprime_imagem('Original', imagem)

nova_imagem = filtro_media(imagem, 1, 3)
imprime_imagem('Filtro da média', nova_imagem)
