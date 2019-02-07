import pygame
import sys
import os

class Personaje(pygame.sprite.Sprite):
    def __init__(self, imagen, pos=[10,10], size=(100,100)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/personajes/" + imagen + "/" + imagen + ".png")
        self.image = pygame.transform.scale(self.image, size)
        
        self.x = pos[0]
        self.y = pos[1]
        self.ancho = size[0]
        self.alto = size[1]

class Fondo(pygame.sprite.Sprite):
    def __init__(self, fondo, pos=[0,0], size=(800,600)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/fondos/" + fondo + ".png")
        self.x = pos[0]
        self.y = pos[1]
        self.ancho = size[0]
        self.alto = size[1]
        

class Pantalla:
    def __init__(self):
        self.sprites = {}
        self.canvas = pygame.display.set_mode((800, 600))
        self.eventos =	{
        "Arriba": False,
        "Abajo": False,
        "Derecha": False,
        "Izquierda": False,
        "Salir":False,
        "Retroceder": False #Pantalla anterior
        }

    def obtener_ultima_pantalla(self):
        pass

    def agregar_sprite(self, nombre, sprite):
        self.sprites[nombre] = sprite
        
    def handle_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.eventos["Salir"]=True
                pygame.quit(); sys.exit()
                print(self.eventos["Salir"])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.eventos["Retroceder"]=True
                    print(self.eventos["Retroceder"])
                if event.key == pygame.K_LEFT:
                    self.eventos["Izquierda"]=True
                    print(self.eventos["Izquierda"])
                if event.key == pygame.K_RIGHT:
                    self.eventos["Derecha"]=True
                    print(self.eventos["Derecha"])
                if event.key == pygame.K_UP:
                    self.eventos["Arriba"]=True
                    print(self.eventos["Arriba"])
                if event.key == pygame.K_DOWN:
                    self.eventos["Abajo"]=True
                    print(self.eventos["Abajo"])

    def update(self):
        for nombre in self.eventos:
            self.eventos[nombre]=False
            #print(self.eventos[nombre])

    def render(self):
        #print("render")
        #self._canvas.fill([0,0,0])
        for nombre, sprite in self.sprites.items():
            surf = pygame.Surface((sprite.ancho,sprite.alto))
            self.canvas.blit(sprite.image, surf.get_rect(topleft=(sprite.x, sprite.y)))
        pygame.display.flip()
    
class Pantalla1(Pantalla):
    def __init__(self):
        Pantalla.__init__(self)
        #Imagenes a usar
        personaje = "hero"
        fondo = "Background"               
        p1 = Personaje(personaje)        
        f1 = Fondo(fondo)

        self.agregar_sprite(fondo,f1)
        self.agregar_sprite(personaje,p1)
        self.handle_events()
        self.update()

class Pantalla2(Pantalla):
    def __init__(self):
        Pantalla.__init__(self)
        #Imagenes a usar
        personaje = "hero"
        fondo = "desert"        
                
        p1 = Personaje(imagen = personaje, pos=[110,110])
        f1 = Fondo(fondo)
        #Este desplazamiento del fondo es solo para probar que ya no se está renderizando 
        #la pantalla anterior
        f1.x = 110
        f1.y = 110

        self.agregar_sprite(fondo,f1)
        self.agregar_sprite(personaje,p1)
        self.handle_events()
        self.update()



'''
He puesto a Bob Esponja solo como referencia, pues la imagen que aparecerá en el menú para elegir personajes
debe ser frontal; mientras que las utilizadas durante el juego per sé serán laterales
'''

# Para crear una pantalla extra (o la de login) se crea una clase como Ejemplo pantalla y se llama 
# desde game.py en la clase ScreenManager

""" class Login(Pantalla):
    def __init__(self, canvas):
        Pantalla.__init__(self, canvas)
        p1 = Personaje("images/personajes/hero/hero1.png")
        self.agregar_sprite("hero1",p1)
        self.handle_events()
        self.update() """

    #def handle_events(self):
       # pass
    #def update(self):
        #self.sprites["hero1"].x += 100
