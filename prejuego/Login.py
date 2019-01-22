import pygame
import os

'''
MARIO
Cuando ya estén las imágenes de los botones, modificas los números 
para que tengan el tamaño y posición adecuados
'''
class Login():
    def __init__(self):
        self.imgs=[]
        self.btns = []
        self.pcs = [(10,10),(50,50),(100,100),(150,150)]    #posición de la esquina superior izquierda
        self.sizes = [(100,40),(100,40),(100,40),(100,40)]  #largo x alto
        self.cargar_imagenes()
        self.dibujar_imagenes()
    
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

    def dibujar_imagenes(self):
        '''
        #(Boton, pos(x,y))
        Modificar las posiciones
        '''        
        b1 = [self.imgs[0], self.pcs[0]] 
        b2 = [self.imgs[1], self.pcs[1]]
        b3 = [self.imgs[2], self.pcs[2]]
        b4 = [self.imgs[3], self.pcs[3]]
        self.btns = [b1, b2, b3, b4]

    


