import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS
from prejuego import Login

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
        self.botones = [] #Almacenará el objeto boton como imagen
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
   

    def cambiar_fondo(self, fondo, titulo="Abajo los corruptos"):
        self.world = pygame.display.set_mode(self.screen_dim)
        pygame.display.set_caption(titulo)  
        self.backdrop = pygame.image.load(os.getcwd() + "/images/menu/" + fondo + ".jpeg").convert()    
        self.backdropbox = self.world.get_rect()


    '''def cargar_botones(self, img_botones=[]):
        self.botones = img_botones.btns'''



    def dibujar_botones(self, img_botones=[], pocs = [] ):        
        k = len(img_botones)
        
        for i in range(k):
            self.world.blit(img_botones[i], pocs[i])
    

    
    def lugar_funcional(self, pos, img_botones=[]):        
        #devuelve si se presionó o no un objeto     
        #pos --> posición del mouse (x,y)
        #img_botones = [esquina, dimensiones]
        
        rango_x = [0,0]
        rango_y = [0,0]
        nr = len(img_botones) #número de img_botones
        
        #El mouse se encuentra en el rango definido previamente
        cx = False 
        cy = False

        #verificar cada región funcional (botones, text_box)
        for i in range(nr):
            #[pos_en_regiones       esq/dim         (x,y)]
            rango_x = [img_botones[i][0][0], img_botones[i][0][0] + img_botones[i][1][0]]
            rango_y = [img_botones[i][0][1], img_botones[i][0][1] + img_botones[i][1][1]]
            
            #definir booleanos
            cx = (pos[0] >= rango_x[0]) and (pos[0] <= rango_x[1] + 1)
            cy = (pos[1] >= rango_y[0]) and (pos[1] <= rango_y[1] + 1)


            #compara la posición del mouse con los rangos establecidos
            if (cx and cy):
                print("Se ha presionado en un lugar funcional")
                #Se modifica el valor de la variable self.obj_pressed
                #self.obj_pressed = 


    def accion_obj_presionado(self, obj):
        pass


    def loopear(self, repetir=True):
        main = repetir
        
        sc_login = Login.Login()
        self.botones = sc_login.imgs
        
        
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
                self.lugar_funcional(pos, [sc_login.pcs, sc_login.sizes])
                if self.obj_pressed != None :
                    self.accion_obj_presionado(self.obj_pressed)
                self.obj_pressed = None

            if self.bool_sgt_pnt:
                self.cambiar_fondo(str_sgt_pnt)
                #Posiblemente main = False
            
            
            #Mantener viva la ventana      
            self.dibujar_botones(sc_login.imgs, sc_login.pcs)
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
