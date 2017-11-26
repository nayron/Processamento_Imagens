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
            valor = int(imagem[i + i, j + j]) + int(imagem[i + i, j + j + 1])
            valor += int(imagem[i + i + 1, j + j]) + int(imagem[i + i + 1, j + j + 1])
            valor /= 4
            nova_imagem[i, j] = valor
    
    return nova_imagem

def bicubica_reducao(imagem):
    """Reduz a imagem usando a interpolação bicubica"""
    nova_imagem = cria_nova_imagem(imagem.shape[0] / 2, imagem.shape[1] / 2)
    
    for i in range(nova_imagem.shape[0]):
        for j in range(nova_imagem.shape[1]):
            if j == nova_imagem.shape[1] - 1 and i != nova_imagem.shape[0] - 1:
                # Borda direita
                valor = int(imagem[i + i, j + j]) + int(imagem[i + i, j + j + 1]) + int(imagem[i + i, j + j + 1])
                valor += int(imagem[i + i + 1, j + j]) + int(imagem[i + i + 1, j + j + 1]) + int(imagem[i + i + 1, j + j + 1])
                valor += int(imagem[i + i + 2, j + j]) + int(imagem[i + i + 2, j + j + 1]) + int(imagem[i + i + 2, j + j + 1])
                valor /= 9
            elif i == nova_imagem.shape[0] - 1 and j != nova_imagem.shape[1] - 1:
                # Borda inferior
                valor = int(imagem[i + i, j + j]) + int(imagem[i + i, j + j + 1]) + int(imagem[i + i, j + j + 2])
                valor += int(imagem[i + i + 1, j + j]) + int(imagem[i + i + 1, j + j + 1]) + int(imagem[i + i + 1, j + j + 2])
                valor += int(imagem[i + i + 1, j + j]) + int(imagem[i + i + 1, j + j + 1]) + int(imagem[i + i + 1, j + j + 2])
                valor /= 9
            elif i == nova_imagem.shape[0] - 1 and j == nova_imagem.shape[1] - 1:
                # Canto inferior direito
                valor = int(imagem[i + i, j + j]) + int(imagem[i + i, j + j + 1]) + int(imagem[i + i, j + j + 1])
                valor += int(imagem[i + i + 1, j + j]) + int(imagem[i + i + 1, j + j + 1]) + int(imagem[i + i + 1, j + j + 1])
                valor += int(imagem[i + i + 1, j + j]) + int(imagem[i + i + 1, j + j + 1]) + int(imagem[i + i + 1, j + j + 1])
                valor /= 9
            else:
                # Todo o resto
                valor = int(imagem[i + i, j + j]) + int(imagem[i + i, j + j + 1]) + int(imagem[i + i, j + j + 2])
                valor += int(imagem[i + i + 1, j + j]) + int(imagem[i + i + 1, j + j + 1]) + int(imagem[i + i + 1, j + j + 2])
                valor += int(imagem[i + i + 2, j + j]) + int(imagem[i + i + 2, j + j + 1]) + int(imagem[i + i + 2, j + j + 2])
                valor /= 9
            
            nova_imagem[i, j] = valor
    
    return nova_imagem

def vizinho_ampliacao(imagem):
    """Amplia a imagem usando a interpolação por vizinho mais próximo"""
    nova_imagem = cria_nova_imagem(imagem.shape[0] * 2, imagem.shape[1] * 2)
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            nova_imagem[i + i, j + j] = imagem[i, j]
            
    for i in range(0, nova_imagem.shape[0], 2):
        for j in range(0, nova_imagem.shape[1], 2):
            nova_imagem[i, j + 1] = nova_imagem[i, j]
            nova_imagem[i + 1, j] = nova_imagem[i, j]
            nova_imagem[i + 1, j + 1] = nova_imagem[i, j]
    
    return nova_imagem
    
def bilinear_ampliacao(imagem):
    """Amplia a imagem usando a interpolação bilinear"""
    nova_imagem = cria_nova_imagem(imagem.shape[0] * 2, imagem.shape[1] * 2)
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            nova_imagem[i + i, j + j] = imagem[i, j]
            
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            a = 0; b = 0; c = 0
            
            if j == imagem.shape[1] - 1 and i != imagem.shape[0] - 1:
                # Borda direita
                a = int(imagem[i, j])
                b = (int(imagem[i, j]) + int(imagem[i + 1, j])) / 2
                c = (int(imagem[i, j]) * 2 + int(imagem[i + 1, j]) * 2) / 4
            elif i == imagem.shape[0] - 1 and j != imagem.shape[1] - 1:
                # Borda inferior
                a = (int(imagem[i, j]) + int(imagem[i, j + 1])) / 2
                b = int(imagem[i, j])
                c = (int(imagem[i, j]) * 2 + int(imagem[i, j + 1]) * 2) / 4
            elif i == imagem.shape[0] - 1 and j == imagem.shape[1] - 1:
                # Canto inferior direito
                a = int(imagem[i, j])
                b = int(imagem[i, j])
                c = int(imagem[i, j])
            else:
                # Todo o resto
                a = (int(imagem[i, j]) + int(imagem[i, j + 1])) / 2
                b = (int(imagem[i, j]) + int(imagem[i + 1, j])) / 2
                c = int(imagem[i, j]) + int(imagem[i, j + 1])
                c += int(imagem[i + 1, j]) + int(imagem[i + 1, j + 1])
                c /= 4
            
            nova_imagem[i + i, j + j + 1] = a
            nova_imagem[i + i + 1, j + j] = b
            nova_imagem[i + i + 1, j + j + 1] = c
    
    return nova_imagem

def bicubico_ampliacao(imagem):
    """Amplia a imagem usando a interpolação bicubica"""
    nova_imagem = cria_nova_imagem(imagem.shape[0] * 2, imagem.shape[1] * 2)
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            nova_imagem[i + i, j + j] = imagem[i, j]
    
    return nova_imagem

#imagem = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
imagem = cv.imread('imagens/lena.bmp')
imprime_imagem('Original', imagem)
imagem = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)

# Métodos de redução
# nova_imagem = cv.cvtColor(vizinho_reducao(imagem), cv.COLOR_GRAY2RGB)
nova_imagem = vizinho_reducao(imagem)
imprime_imagem('Redução por vizinho mais próximo', nova_imagem)

nova_imagem = bilinear_reducao(imagem)
imprime_imagem('Redução bilinear', nova_imagem)

nova_imagem = bicubica_reducao(imagem)
imprime_imagem('Redução bicubica', nova_imagem)

# Métodos de aumento
nova_imagem = vizinho_ampliacao(imagem)
imprime_imagem('Ampliação por vizinho mais próximo', nova_imagem)

nova_imagem = bilinear_ampliacao(imagem)
imprime_imagem('Ampliação bilinear', nova_imagem)

# nova_imagem = bicubico_ampliacao(imagem)
# imprime_imagem('Ampliação bicubica', nova_imagem)
