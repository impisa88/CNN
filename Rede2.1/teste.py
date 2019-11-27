##!/usr/bin/env python
# -*- coding: UTF-8 -*-

import glob
import os
from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import rasterio as ras

tamanho = 128

os.chdir("C:\\Users\\joaosh\\Downloads\\DATASET")

lista = os.listdir("C:\\Users\\joaosh\\Downloads\\DATASET\\Carboidrato")
file_count = len(lista)
nome = 0

while file_count > 0:

    for file in glob.glob("*.jpg"):

        img = Image.open(file).convert('L') #converte em escala de cinza

        img = img.resize((tamanho,tamanho), Image.ANTIALIAS) # deixa a imagem em 128x128 

        array = img.ras()
        print(array)

        img.save('proteina' + str(nome) + '.jpg') #salva imagem com nome = prato.numero
        #img.save('carboidrato' + str(nome) + '.jpg') #salva imagem com nome = errado'.numero
        #img.save('legumes' + str(nome) + '.jpg') #salva imagem com nome = errado'.numero
        #img.save('outros' + str(nome) + '.jpg') #salva imagem com nome = errado'.numero
        nome = nome+1
        file_count = file_count - 1
