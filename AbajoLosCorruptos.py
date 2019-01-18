import VentanasMenu as vm
import ScreenMaster as sm

def main():
    abc = sm.ScreenMaster()
    #abc = vm.VentanasMenu()
    abc.cambiar_fondo("login")
    abc.loopear()


if __name__ == "__main__":
    main()

