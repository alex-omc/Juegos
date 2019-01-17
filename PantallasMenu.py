import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS

class VentanasMenu():
    bkg = sys.argv = [1]
    
    def __init__(self, bkg):
        #self.bakg = bkg #background
        self.main = True
    
    #Crear ventana
    worldx = 1280
    worldy = 800
    fps   = 40  # frame rate
    ani   = 4   # animation cycles
    clock = pygame.time.Clock()
    pygame.init()
    world    = pygame.display.set_mode([worldx,worldy])
    #self.main = True

    #cargar fondo de login
    backdrop = pygame.image.load("Images/menu/" + str(bkg) + ".jpeg").convert()
    backdropbox = world.get_rect()

    #Coordenadas de las esquinas de los botones
    #el orden es [esz.sup.izq, ancho(px), alto(px)]
    btn_registrar = [0,0,0]    
    btn_fotgot_password = [0,0,0]
    btn_creditos = [0,0,0]
    btn_quit = [0,0,0]


    def detectar_posicion(self, pos, pres):
        #Verificar en qué lugar se hizo click
        #Pos is the mouse position or a tuple of (x,y) coordinates
        #pres indica si si el botón del mouse está presionado
        arr_bool = [False, False, False, False]
        k = 0
        b1 = False
        b2 = False
        for i in range[ btn_registrar, btn_fotgot_password, btn_creditos, btn_quit]:
            b1 = (pos[0] in range(i[0], i[0] + i[1] + 1))
            b2 = (pos[1] in range(i[0], i[0] + i[2] + 1))   
            arr_bool[k] = b1 and b2
            k += 1         
        
        if arr_bool[0] :
            #registrar
            pass
        elif arr_bool[1]:
            #Registrar usuario
            pass
        elif arr_bool[2]:
            #Recuperar contraseña
            pass
        elif arr_bool[3]:
            #salir
            aelf.main = False
 


    while self.main == True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                presionado = True            
            
            detectar_posicion(pos, presionado)


            '''
            FALTA CODIFICAR LA PARTE DE ESCRITURA EN LOS TEXTBOX
            '''

        
        





    world.blit(backdrop, backdropbox)    
    pygame.display.flip()
    clock.tick(fps)


'''
El método para ubicación y click del mouse fue tomada del siguiente video
https://www.youtube.com/watch?v=4_9twnEduFA&lc=Ugx9T3FeyrQZpRJV_wl4AaABAg
'''
    