#Crear la clase nodo
class node:
    #Crear el constructor de la clase
    def __init__(self,datoQueVieneDelMain = None, punteroQueVienedelMain = None):
        self.data= str(datoQueVieneDelMain)
        self._next= punteroQueVienedelMain
    
    #Metodo para visusaliar la infrmacion
    def __str__(self):
        return str(self.data)
