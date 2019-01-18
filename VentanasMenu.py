import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS

class VentanasMenu(pygame.sprite.Sprite):    
     
    def __init__(self, bkg="login", tipo_interfaz=1):
        self.fondo = bkg #background
        self.tipo_interfaz = tipo_interfaz #cantidad de textbox
        
        self.world = 0
        self.backdrop = 0
        self.backdropbox = 0
        self.clock = 0
        self.fps   = 60  # frame rate
        self.screen_dim = [1280, 800]
        self.clock = pygame.time.Clock()
        pygame.init()


        
    def lugar_presionado(self, posX=0, posY=0):
        '''
        posX --> Posición del mouse en el eje X
        posY --> Posición del mouse en el eje Y
        -----------------------------------------------------------------------
        Medidas de los dim_btn en píxeles 
        btn_registrar / btn_fotgot_password 
        btn_creditos / btn_quit
        el orden es [esz.sup.izq (px), ancho(px), alto(px)]
        '''
        continuar = True
        '''
        Las dimensiones y posiciones siempre son las mismas, por eso se
        declaran acá en la clase padre
        '''
        dim_btn = [[0,1,2],[0,1,2],[0,1,2],[100,20,50]]
        bool_btn = [False, False, False, False]

        #Botones
        k = 0
        b1 = False
        b2 = False
        #for i in range[btn_registrar, btn_fotgot_password, btn_creditos, btn_quit]:
        for i in range(0,4):
            b1 = (posX in range(dim_btn[i][0], dim_btn[i][0] + dim_btn[i][1] + 1))
            b2 = (posY in range(dim_btn[i][0], dim_btn[i][0] + dim_btn[i][2] + 1))   
            bool_btn[k] = (b1 and b2) 
            k += 1         
        
        if bool_btn[0] :           #registrar
            pass
        elif bool_btn[1]:           #Registrar usuario
            pass
        elif bool_btn[2]:           #Recuperar contraseña
            pass
        elif bool_btn[3]:           
            pygame.quit(); sys.exit()
            continuar = False
        
        return continuar

            

    def escribir_txt(self, posX=0, posY=0, tif=1):
        '''
        tif --> Tipo de interface, el número depende de la 
        cantidad de textbox que tenga el menu en presente
        '''
        
        
        #Text Box
        if (tif == 1):
            pass
        else:
            #El segundo textbox debe estar con formato contraseña
            #es decir que muestre puntos al escribir
            pass

    def cambiar_fondo(self, fondo="login"):
        #Crear ventana
        
        ani   = 4   # animation cycles        

        self.world = pygame.display.set_mode(self.screen_dim)
        #cargar fondo de login        
        self.backdrop = pygame.image.load(os.getcwd() + "/images/menu/" + fondo + ".jpeg").convert()    
        self.backdropbox = self.world.get_rect()
        
 
 
    
    def loopear(self):
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
                
                if pres: 
                    #pnt = lugar_presionado(pos[0], pos[1], self.tipo_interfaz)
                    pnt = self.lugar_presionado(pos[0], pos[1])
                    

                '''
                FALTA CODIFICAR LA PARTE DE ESCRITURA EN LOS TEXTBOX
                '''


            self.world.blit(self.backdrop, self.backdropbox)    
            pygame.display.flip()
            self.clock.tick(self.fps)

'''
def main():
    print(3 * "\n")
    print("Hola desde el main")
    abc = VentanasMenu()
    abc.cambiar_fondo("login")
    abc.loopear()

if __name__ == "__main__":
    main()
'''        





    


'''
El método para ubicación y click del mouse fue tomada del siguiente video
https://www.youtube.com/watch?v=4_9twnEduFA&lc=Ugx9T3FeyrQZpRJV_wl4AaABAg
'''
    