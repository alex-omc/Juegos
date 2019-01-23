import cryptography as cr
#import numpy
import random


class Servidor():
    '''
    Criptografía Asimétrica
        fuente n°1 = https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
        fuente n°2 = https://cryptography.io/en/latest/hazmat/primitives/asymmetric/utils/?highlight=hazmat
    
    
    Criptografía Simétrica
        fuente n°3 = https://cryptography.io/en/latest/fernet/
    '''
    
    def __init__(self):
        self.players = []
        self.ip_players = []
        self.symmetric_keys=[]
        self.public_key
        self.private_key
        


    def generar_par_de_claves(self):
        '''
        Ver cómo funciona IKEv2, o sea el órden
        '''
        #El cliente usará la clave pública para enviar la tupla (user, password)
        #Código obtenido de fuente n°1
        self.private_key = cr.hazmat.primitives.asymmetric.rsa.generate_private_key( public_exponent=65537,
                        key_size=2048, backend=cr.hazmat.backends.default_backend())
        self.public_key = self.private_key.public_key()
          

    def generar_llaves_simetricas(self):
        pass
    
    
    def validar_usuario(self, usuario='', psw=''):
        #hacer la consulta correspondiente con la base de datos
        #En este punto los datos YA ESTÁN desencriptados
        pass

    def nuevo_psw(self, usuario='', psw=''):
        #Establecer un nuevo password para el usuario
        #En este punto los datos YA ESTÁN desencriptados
        pass


    def add_player(self, player):
        self.players.append(player)
    

    def elegir_escenario(self, esc=[]):
        if random.random() < 0.5:
            return esc[0]
        else:
            return esc[1]

   
    
    def enviar_mensaje_encriptado(self, destino, mensaje = ''):
        pass


    def desencriptar_mensaje(self, remitente, mensaje = ''):
        pass
    

