# -*- coding: utf-8 -*-
# Projeto 1 - Processamento de imagens

from __future__ import print_function
from random import randint
from Tkinter import *

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class Rotulo(object):
    """Define a estrutura de um rótulo"""
    
    def __init__(self, nome, posicoes):
        self.nome = nome
        self.posicoes = posicoes

def imprime_imagem(tipo, imagem):
    """Monta a imagem novamente e imprime"""
    cv.imshow(tipo, imagem)
    cv.waitKey(0)
    cv.destroyAllWindows()

def quantiza(imagem):
    """Executa o algoritmo de quantização na imagem"""
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if imagem[i, j] < 127:
                imagem[i, j] = 0
            else:
                imagem[i, j] = 255
    return imagem

def rotula(imagem):
    """Executa o algoritmo de rotulação de regiões"""
    rotulo = 0
    equivalentes = []
    matriz_rotulos = np.zeros((imagem.shape[0], imagem.shape[1]))
    
    # 0 = preto   ;   255 = branco
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if imagem[i, j] == 0:
                if imagem[i, j - 1] == 255 and imagem[i - 1, j] == 255:
                    rotulo += 1
                    matriz_rotulos[i, j] = rotulo
                elif imagem[i, j - 1] == 0 and imagem[i - 1, j] == 255:
                    matriz_rotulos[i, j] = matriz_rotulos[i, j - 1]
                elif imagem[i, j - 1] == 255 and imagem[i - 1, j] == 0:
                    matriz_rotulos[i, j] = matriz_rotulos[i - 1, j]
                elif matriz_rotulos[i, j - 1] == matriz_rotulos[i - 1, j]:
                    matriz_rotulos[i, j] = matriz_rotulos[i, j - 1]
                else:
                    matriz_rotulos[i, j] = matriz_rotulos[i, j - 1]
                    rotulos = (matriz_rotulos[i, j-1], matriz_rotulos[i - 1, j])
                    if not equ_ja_adicionado(rotulos, equivalentes):
                        equivalentes.append(rotulos)
    
    rotulos = resolve_equivalencias(matriz_rotulos, equivalentes, rotulo)
    imprime_resultados(matriz_rotulos, equivalentes, rotulos, rotulo)
    imagem = rotulos_para_imagem(matriz_rotulos, rotulos)
    
    return imagem

def equ_ja_adicionado(rotulos, equivalentes):
    """Checa se os rotulos já foram adicionados na lista de equivalentes"""
    for i in range(len(equivalentes)):
        if equivalentes[i] == rotulos or equivalentes[i] == reversed(rotulos):
            return True
    return False

def resolve_equivalencias(matriz_rotulos, equivalentes, ultimo_rotulo):
    """Checa se existem rótulos equivalentes e os resolve"""
    
    for tupla in equivalentes:
        tupla
    
    return rotulos

def imprime_resultados(matriz_rotulos, equivalentes, rotulos, rotulo):
    """Imprime os dados resultantes do processamento"""
    print("- Foram usados " + str(rotulo) + " rotulos no processamento.")
    
    print("\n- Os rótulos são: ")
    for i in range(0, rotulo):
        print(str(i + 1) + ", ", end='')
    
    print("\n\n- Equivalências: ")
    for i in range(0, len(equivalentes)):
        print(str(equivalentes[i]) + "; ", end='')
    
    print("\n\n- Após a resolução das equivalências sobram os rótulos: ")
    for rotulo in rotulos.keys():
        print(str(rotulo) + "; ", end='')
    print("\n")
    
    print("- Matriz final:")
    for i in range(matriz_rotulos.shape[0]):
        for j in range(matriz_rotulos.shape[1]):
            print(str(matriz_rotulos[i, j]) + ", ", end='')
        print("\n")
    
    # linhas = []
    # i = 0
    # for rotulo in rotulos.keys():
    #     colunas = []
        
    #     e = Entry(relief = RIDGE)
    #     e.grid(row = i, column = 0, sticky = NSEW)
    #     e.insert(END, rotulo)
        
    #     colunas.append(e)
    #     i += 1
        
    #     linhas.append(colunas)
    
    # mainloop()

def rotulos_para_imagem(matriz_rotulos, rotulos):
    """Converte a matriz de rótulos para uma imagem colorida que representa as regiões"""
    regioes = np.empty((matriz_rotulos.shape[0], matriz_rotulos.shape[1]), np.uint8)
    regioes[:, :] = 255
    cores = {}
    
    for rotulo in rotulos:
        cores[rotulo] = [randint(0, 200), randint(0, 200), randint(0, 200)]
    
    for i in range(matriz_rotulos.shape[0]):
        for j in range(matriz_rotulos.shape[1]):
            for rotulo, cor in cores.items():
                if matriz_rotulos[i, j] == rotulo:
                    regioes[i, j] = cor[0]
    
    return regioes

imagem = cv.imread('imagem4.png')
imprime_imagem("Imagem original", imagem)
imagem = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)

imagem = quantiza(imagem)
imprime_imagem("Imagem quantizada", imagem)

imagem = rotula(imagem)
imprime_imagem("Imagem dividida por regiões", imagem)
