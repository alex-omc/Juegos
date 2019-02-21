import pygame
import Player as pl
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

'''class Animacion(pygame.sprite.Sprite):  
    def set_animaciones(self):        
        for i in range(1, 11):
            img = pygame.image.load(os.path.join('images/personajes/' + str(self.player_id), str(self.player_id) + str(i) + '.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey((255,255,255))  # set alpha'''

class Fondo(pygame.sprite.Sprite):
    def __init__(self, fondo, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/fondos/" + fondo + ".png")    
        self.image = pygame.transform.scale(self.image, Pantalla.resolucion())
        self.x = pos[0]
        self.y = pos[1]
        self.ancho = Pantalla.resolucion()[0]
        self.alto = Pantalla.resolucion()[1]
        

class Pantalla:
    def __init__(self):
        self.sprites = {}
        self.canvas = pygame.display.set_mode(self.resolucion())
        self.eventos =	{
        "Retroceder": False, #Pantalla anterior
        "Arriba": False,
        "Abajo": False,
        "Derecha": False,
        "Izquierda": False,
        "Salir": False,        
        "POSX": 0,
        "POSY": 0
        }

    @classmethod
    def resolucion(cls):
        return (800, 600)
    
    def set_nombre_ventana(self, titulo):
        pygame.display.set_caption(titulo)
    
    def obtener_ultima_pantalla(self):
        pass

    def agregar_sprite(self, nombre, sprite):
        self.sprites[nombre] = sprite

    def reproducir_sonido(self, musica): #musica es el archivo de sonido, este solo sonara una vez ej: disparos
        #pygame.mixer.music.load(os.getcwd() + "/Audios/Animaciones/" + musica + ".mp3")
        s = pygame.mixer.Sound(os.getcwd() + "/Audios/Animaciones/" + musica + ".wav")
        pygame.mixer.Sound.play(s)

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
                    self.reproducir_sonido("Golpe")
                    print(self.eventos["Derecha"])
                if event.key == pygame.K_UP:
                    self.eventos["Arriba"]=True
                    self.reproducir_sonido("HeadShot")
                    print(self.eventos["Arriba"])
                if event.key == pygame.K_DOWN:
                    self.eventos["Abajo"]=True
                    print(self.eventos["Abajo"])
            if event.type == pygame.MOUSEBUTTONUP:
                self.eventos["POSX"]=str(pygame.mouse.get_pos()[0])
                self.eventos["POSY"]=str(pygame.mouse.get_pos()[1])
                print(self.eventos["POSX"])
                print(self.eventos["POSY"])


    def update(self):
        for nombre in self.eventos:
            self.eventos[nombre]=False
            #print(self.eventos[nombre])

    def render(self):
        #print("render")
        #self._canvas.fill([0,0,0])
        for nombre, sprite in self.sprites.items():
            surf = pygame.Surface((sprite.ancho, sprite.alto))
            self.canvas.blit(sprite.image, surf.get_rect(topleft=(sprite.x, sprite.y)))
        pygame.display.flip()
    
class Pantalla1(Pantalla):
    def __init__(self):        
        Pantalla.__init__(self)
        #Imagenes a usar
        personaje = "hero"
        fondo = "Fondo1"               
        p1 = Personaje(personaje)        
        f1 = Fondo(fondo)
        
        self.set_nombre_ventana("Pantalla 1")
        self.agregar_sprite(fondo,f1)
        self.agregar_sprite(personaje,p1)
        self.handle_events()
        self.update()
        

class Pantalla2(Pantalla):
    def __init__(self):
        Pantalla.__init__(self)
        #Imagenes a usar
        personaje = "alan"
        fondo = "Fondo2"
        jugador = "hero"
        p1 = Personaje(imagen = personaje, size=(63, 125), pos=[450,450])        
        f1 = Fondo(fondo = fondo, pos = [50, 50])
        j1 = pl.Player(jugador)

        self.set_nombre_ventana("Pantalla 2")
        self.agregar_sprite(fondo, f1)
        self.agregar_sprite(personaje, p1)
        self.agregar_sprite(jugador, j1)
        self.handle_events()
        self.update()






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