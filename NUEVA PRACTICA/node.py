class node:
    #Crear constructor
    def __init__(self ,datoQuevieneDelMain = None, punteroQueVieneDelMain = None):
        self.data = datoQuevieneDelMain
        self._next = punteroQueVieneDelMain

    #Metodo para crear la informacion
    def __str__(self):
        return str(self.data)