import ScreenMaster as sm
#import pygame


def main():
    prejuego = True
    secuencia_principal = [('login','Abajo los corruptos'),
                          ('personajes','Abajo los corruptos'),
                          ('escenario','Abajo los corruptos')]


    abc = sm.ScreenMaster()
    abc.cambiar_fondo(secuencia_principal[0][0],secuencia_principal[0][1])
        
    abc.loopear(prejuego)

    #ejecutar ek engine





if __name__ == "__main__":
    main()

