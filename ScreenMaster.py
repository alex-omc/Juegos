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
        self.screen_dim = [1280, 800]
        self.iniciar_pantalla()
        self.fondo = ""
        self.bool_sgt_pnt = False #Cambiar a la siguiente pantalla
        self.botones = [] #Almacenará el objeto boton, y el area que ocupa (tupla esq-largo-ancho)
        self.textos = [] #Almacenará el objeto boton, y el area que ocupa (tupla esq-largo-ancho)
        self.obj_pressed = None #Indica que objeto está siendo presionado en un momento determinado
        self.mensaje = ["mensaje", 0] #es el texto que se va a enviar al motor (0), y de ser el caso reenviado al servidor(1)

        self.world = 0
        self.backdrop = 0
        self.backdropbox = 0
        self.clock = 0
        self.fps   = 60  # frame rate        
        self.clock = pygame.time.Clock()


    def iniciar_pantalla(self):            
        ani   = 4   # animation cycles
        clock = pygame.time.Clock()
        pygame.init()    
        world = pygame.display.set_mode(self.screen_dim)

        


    def add_btn(self, pos=(0,0), ancho=20, alto=10, fondo="", texto="abc"):
        #los a=B son el valor predeterminado en caso no se envíe el parámetro
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
        self.world = pygame.display.set_mode(self.screen_dim)   
        self.backdrop = pygame.image.load(os.getcwd() + "/images/menu/" + fondo + ".jpeg").convert()    
        self.backdropbox = self.world.get_rect()

    

    def lugar_funcional(self, pos):        
        #devuelve si se presionó o no un objeto     
        #De ser el caso se modifica el valor de la variable self.obj_pressed
        pass

    def accion_obj_presionado(self, obj):
        pass


    def loopear(self):
        main = True
        while main:
            pres = False # Botón izq del mouse presionado
            str_sgt_pnt = "" #Nombre del siguiente fondo a cargar

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
                self.lugar_funcional(pos)
                if self.obj_pressed != None :
                    self.accion_obj_presionado(self.obj_pressed)
                self.obj_pressed = None

            if self.bool_sgt_pnt:
                self.cambiar_fondo(str_sgt_pnt)
                #Posiblemente main = False
            
            
            #Mantener viva la ventana                
            self.world.blit(self.backdrop, self.backdropbox)    
            pygame.display.flip()
            self.clock.tick(self.fps)





'''       
def main():
    print(3 * "\n")
    print("Hola desde el main")
    abc = ScreenMaster()
    abc.cambiar_fondo("login")
    abc.loopear()

if __name__ == "__main__":
    main()
    
'''    
