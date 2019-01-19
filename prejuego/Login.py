import pygame
import sys
import os

'''
Orden de los valores
(posicion), (ancho, alto), fondo, texto

btn_registrar = [(0,0),(0,0),(0,0,0),"Registrar"]
btn_olvide = [(0,0),(0,0),(0,0,0),"Olvide contraseña"]
btn_creditos = [(0,0),(0,0),(0,0,0),"creditos"]
btn_salir = [(0,0),(0,0),(0,0,0),"Salir"]
botones = [btn_registrar, btn_olvide, btn_creditos, btn_salir]
'''

btn_registrar = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
btn_olvide = pygame.image.load(os.getcwd() + "/images/botones/.png")
btn_creditos = pygame.image.load(os.getcwd() + "/images/botones/.png")
btn_salir = pygame.image.load(os.getcwd() + "/images/botones/salir.png")












'''
Orden de los valores
(posicion), (ancho, alto), tipo
    tipo 0 usuario
    tipo 1 password
'''