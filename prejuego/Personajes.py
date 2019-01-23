import pygame
import os

'''
MARIO
Cuando ya estén las imágenes de los botones, modificas los números 
para que tengan el tamaño y posición adecuados
'''
class Personajes():
    def __init__(self):
        self.imgs=[] #imágenes de los botones
        self.btns = [] #bones[(imagen, posicion)]
        self.pcs = [(0,0),(350,180),(700,360),(1050,540)]    #posición de la esquina superior izquierda
        self.sizes = [(200,100),(200,100),(200,100),(200,100)]  #largo x alto
        self.cargar_imagenes()

    

    def cargar_imagenes(self):
        #Cargar a memoria las imágenes de los botones
        btn_0 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        btn_1 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        btn_2 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        btn_3 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")

        '''
        #Darles el tamaño apropiado
        Modificar los tamaños
        '''        
        btn_registrar = pygame.transform.scale(btn_0, self.sizes[0])
        btn_olvide = pygame.transform.scale(btn_1, self.sizes[1])
        btn_creditos = pygame.transform.scale(btn_2, self.sizes[2])
        btn_salir = pygame.transform.scale(btn_3, self.sizes[3])
        self.imgs = [btn_registrar, btn_olvide, btn_creditos, btn_salir]