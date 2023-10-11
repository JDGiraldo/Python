#Crear la clase
class Node:
    #Creamos el constructor de la clase
    def __init__(self. dataQueVieneDelMain= None. punteroQueVieneDelMain= None):
        self.data=dataQueVieneDelMain
        self._next= punteroQueVieneDelMain

    #Metodo para visualizar la informacion
    def __str__(self):
        return str(self.data)