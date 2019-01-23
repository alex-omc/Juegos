import ScreenMaster as sm
from prejuego import Login, Escenarios, Personajes
#import pygame


def main():
    #prejuego = True
    sc_login = Login.Login()
    sc_personajes = Personajes.Personajes()
    sc_escenarios = Escenarios.Escenarios()

    secuencia_principal = [('login','Abajo los corruptos'),
                          ('personajes','Abajo los corruptos'),
                          ('escenario','Abajo los corruptos')]


    abc = sm.ScreenMaster(sc_login)
    abc.cambiar_fondo(secuencia_principal[0][0],secuencia_principal[0][1])
        
    #abc.loopear(prejuego)
    while True:
        abc.loopear_2(True)

    #ejecutar el engine





if __name__ == "__main__":
    main()

