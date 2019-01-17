import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS

class VentanasMenu(pygame.sprite.Sprite):    
     
    def __init__(self):
        self.bakg = "bkg" #background
        
    
    #Crear ventana
    worldx = 1280
    worldy = 800
    fps   = 40  # frame rate
    ani   = 4   # animation cycles
    clock = pygame.time.Clock()
    pygame.init()
    world = pygame.display.set_mode([worldx,worldy])
 

    #cargar fondo de login
    backdrop = pygame.image.load(os.getcwd() + "/images/menu/" + "login" + ".jpeg").convert()
    #backdrop = pygame.image.load("images/menu/" + "Background" + ".png").convert()
    backdropbox = world.get_rect()


    def detectar_posicion(self, posX, posY):
        '''
        print(pos)
        print("\nPosicion 0 de pos es " + str(pos[0]))
        print("\nPosicion 1 de pos es " + str(pos[1]))
        '''


        '''
        Medidas de los botones en píxeles        
        btn_registrar / btn_fotgot_password 
        btn_creditos / btn_quit
        el orden es [esz.sup.izq (px), ancho(px), alto(px)]
        '''
      
        medidas = [[0,1,2],[0,1,2],[0,1,2],[0,1,2]]

        arr_bool = [False, False, False, False]
        k = 0
        b1 = False
        b2 = False
        #for i in range[btn_registrar, btn_fotgot_password, btn_creditos, btn_quit]:
        for i in range(0,4):
            b1 = (pos[0] in range(medidas[i][0], medidas[i][0] + medidas[i][1] + 1))
            b2 = (pos[1] in range(medidas[i][0], medidas[i][0] + medidas[i][2] + 1))   
            arr_bool[k] = (b1 and b2)
            print(k)
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
            pygame.quit(); sys.exit()
            



    pnt = True #pantalla
    while pnt:
        
        for event in pygame.event.get():
            #Verificar en qué lugar está el mouse, 
            #retorna una tupla (x,y) de coordenadas            
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                pnt = False

            pres = False

            #Verificar si el botón del mouse está presionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                pres = True            
            
            '''
            print("\n\nPos tiene una longitud de " + str(len(pos)))
            print("\n" + str(pos))
            print("Posicion 0 de pos es " + str(pos[0]))
            print("Posicion 1 de pos es " + str(pos[1]) + "\n")
            '''

            if pres: 
                detectar_posicion(pos[0], pos[1])


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
    