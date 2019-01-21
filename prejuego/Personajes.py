import pygame
import os

'''
MARIO
Cuando ya estén las imágenes de los botones, modificas los números 
para que tengan el tamaño y posición adecuados
'''
#Cargar a memoria las imágenes de los botones
btn_registrar = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
btn_olvide = pygame.image.load(os.getcwd() + "/images/botones/.png")
btn_creditos = pygame.image.load(os.getcwd() + "/images/botones/.png")
btn_salir = pygame.image.load(os.getcwd() + "/images/botones/salir.png")
btn_registrar = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
btn_olvide = pygame.image.load(os.getcwd() + "/images/botones/.png")
btn_creditos = pygame.image.load(os.getcwd() + "/images/botones/.png")
btn_salir = pygame.image.load(os.getcwd() + "/images/botones/salir.png")
btn_registrar = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
btn_olvide = pygame.image.load(os.getcwd() + "/images/botones/.png")


'''
#Darles el tamaño apropiado
Modificar los tamaños
'''
sizes = []
btn_registrar = pygame.transform.scale(btn_registrar, (100,40))
btn_olvide = pygame.transform.scale(btn_olvide, (100,40))
btn_creditos = pygame.transform.scale(btn_creditos, (100,40))
btn_salir = pygame.transform.scale(btn_salir, (100,40))
btn_registrar = pygame.transform.scale(btn_registrar, (100,40))
btn_olvide = pygame.transform.scale(btn_olvide, (100,40))
btn_creditos = pygame.transform.scale(btn_creditos, (100,40))
btn_salir = pygame.transform.scale(btn_salir, (100,40))
btn_registrar = pygame.transform.scale(btn_registrar, (100,40))
btn_olvide = pygame.transform.scale(btn_olvide, (100,40))


'''
#(Boton, pos(x,y))
Modificar las posiciones
'''
pcs = [] 
b1 = [btn_registrar, (0,0)] 
b2 = [btn_registrar, (0,0)]
b3 = [btn_registrar, (0,0)]
b4 = [btn_registrar, (0,0)]
#btns = [b1, b2, b3, b4]