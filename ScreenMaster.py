import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS

'''
pygame debe tener librerías con estas funcionalidades, pero 
solo encontré para dibujar formas geométricas
    #import Boton as btn
    #import CajaTexto as txb
'''


class ScreenMaster(pygame.sprite.Sprite): 

    def __init__(self):
        self.fondo = ""
        self.botones = []
        self.textos = []
        self.obj_pressed = []

        #ani   = 4    animation cycles
        #cambiar_fondo("login")
    
    def add_btn(self, pos=(0,0), ancho=20, alto=10, fondo=(0,255,0), texto="abc"):
        #los a=B son el valor predeterminado en caso no se envíe el parámetro
        #fondo también puede ser una imagen, para el caso de los personajes y escenarios 
        '''
        Ete video puede sere de ayuda
        https://www.youtube.com/watch?v=4_9twnEduFA&lc=Ugx9T3FeyrQZpRJV_wl4AaABAg
        O el que pasó mario
        '''       
        pass


    def add_txt(self, pos=(0,0), ancho=20, alto=10, tipo=0):
        # tipo 0 --> texto normal
        # tipo 1 --> contraseña
        pass


    def borrar_todo(self):
        #self.botones = []
        #self.textos = []
        pass
            
    
    def cambiar_fondo(self, fondo):
        pass
    
    def objeto_presionado(self, pos):        
        #devuelve si se presionó o no un objeto        
        #De ser el caso se modifica el valor de la variable self.obj_pressed
        #y el boolean devuelto es False
        pass

    main = True
    while main:
        pres = False #btn izq presionado

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                main = False            
            
            #Verificar si el botón del mouse está presionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                pres = True
            
            #######################
            #######################
            ###presionar  enter####
            #######################
            #######################    

        if pres:
            #retorna una tupla (x,y) de las coordenadas del mouse
            pos = pygame.mouse.get_pos()

            #verificar si se presionó sobre un botón o caja de texto
            #realizar la acción correspondiente
            #Posiblemente main = False
        '''
        Mantener viva la ventana
        '''
            

        
        
    
    
    
    
    
    
    
    
    
    '''
        #cargar fondo de login        
        fps   = 60 
        worldx = 1280
        worldy = 800
        clock = pygame.time.Clock()
        pygame.init()
        world = pygame.display.set_mode([self.worldx, self.worldy])        
        fondo_provisional = "login"
        backdrop = pygame.image.load(os.getcwd() + "/images/menu/" + fondo_provisional + ".jpeg").convert()    
        backdropbox = world.get_rect()
        
        while True:
            world.blit(backdrop, backdropbox)    
            pygame.display.flip()
            clock.tick(60)
    '''
