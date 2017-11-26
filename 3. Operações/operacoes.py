# -*- coding: utf-8 -*-
# Projeto 3 - Processamento de imagens

from __future__ import print_function

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
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

def corrige(valor):
    """Corrige o valor da cor ao ajustá-la aos limites de 0 à 255"""
    if valor < 0:
        return 0
    elif valor > 255:
        return 255
    else:
        return valor

def dentro_das_bordas(x, y, altura, largura):
    """Verifica se os valores de x e y estão dentro das bordas da imagem"""
    if (x >= 0 and x < largura) and (y >= 0 and y < altura):
        return True
    else:
        return False

def adicao(imagem1, imagem2):
    """Executa a operação de adição nas imagens"""
    nova_imagem = cria_nova_imagem(imagem1.shape[0], imagem1.shape[1])
    
    for i in range(imagem1.shape[0]):
        for j in range(imagem1.shape[1]):
            nova_imagem[i, j][0] = corrige(int(imagem1[i, j][0]) + int(imagem2[i, j][0]))
            nova_imagem[i, j][1] = corrige(int(imagem1[i, j][1]) + int(imagem2[i, j][1]))
            nova_imagem[i, j][2] = corrige(int(imagem1[i, j][2]) + int(imagem2[i, j][2]))
    
    return nova_imagem

def subtracao(imagem1, imagem2):
    """Executa a operação de subtração nas imagens"""
    nova_imagem = cria_nova_imagem(imagem1.shape[0], imagem1.shape[1])
    
    for i in range(imagem1.shape[0]):
        for j in range(imagem1.shape[1]):
            nova_imagem[i, j][0] = corrige(int(imagem1[i, j][0]) - int(imagem2[i, j][0]))
            nova_imagem[i, j][1] = corrige(int(imagem1[i, j][1]) - int(imagem2[i, j][1]))
            nova_imagem[i, j][2] = corrige(int(imagem1[i, j][2]) - int(imagem2[i, j][2]))
    
    return nova_imagem

def translacao(imagem, valor):
    """Executa a operação de translação na imagem"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            x = i + valor
            y = j + valor
            if (dentro_das_bordas(x, y, imagem.shape[0], imagem.shape[1])):
                nova_imagem[x, y] = imagem[i, j]
    
    return nova_imagem

def rotacao(imagem, grau):
    """Executa a operação de rotação anti-horária na imagem"""
    nova_imagem = cria_nova_imagem(imagem.shape[0], imagem.shape[1])
    
    ponto = [imagem.shape[0] / 2, imagem.shape[1] / 2]
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            x = int((math.cos(grau) * (i - 256)) + (-math.sin(grau) * (j - 256)) + 256)
            y = int((math.sin(grau) * (i - 256)) + (math.cos(grau) * (j - 256)) + 256)
            
            if (dentro_das_bordas(x, y, imagem.shape[0], imagem.shape[1])):
                nova_imagem[x, y] = imagem[i, j]
            
    return nova_imagem

imagem1 = cv.imread('../Imagens/lena.bmp')
imagem2 = cv.imread('../Imagens/lena_modificada.bmp')

nova_imagem = adicao(imagem1, imagem2)
# imprime_imagem('Adição', nova_imagem)

nova_imagem = subtracao(imagem1, imagem2)
# imprime_imagem('Subtração', nova_imagem)

nova_imagem = translacao(imagem1, 200)
# imprime_imagem('Translação', nova_imagem)

nova_imagem = rotacao(imagem1, math.radians(90))
imprime_imagem('Rotação', nova_imagem)
