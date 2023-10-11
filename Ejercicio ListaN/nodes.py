#Crear la clase nodo
class node:
    #Crear el constructor de la clase
    def __init__(self, datoQueVieneDelMain = None, punteroQueVieneDelMain = None):
        self.data = str(datoQueVieneDelMain)
        self._next = punteroQueVieneDelMain

    #Metodo para visulizar la informacion
    def __str__(self):
        return self.data