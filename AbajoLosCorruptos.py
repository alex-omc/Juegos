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


    ventana_juego = sm.ScreenMaster(sc_login)
    ventana_juego.cambiar_fondo(secuencia_principal[0][0],secuencia_principal[0][1])
        


    #ventana_juego.loopear(True, 'login')    
    
    ventana_juego.objeto.cargar_imagenes()
    while True:
        ventana_juego.loopear_2(True, secuencia_principal[0][0]) 
    


    '''
    #while not ventana_juego.bool_sgt_pnt:
    #    ventana_juego.loopear_2(not ventana_juego.bool_sgt_pnt)

    #ventana_juego.set_objeto(sc_personajes)
    #ventana_juego.cambiar_fondo(secuencia_principal[1][0],secuencia_principal[1][1])

    
    #ejecutar el engine
    '''





if __name__ == "__main__":
    main()

