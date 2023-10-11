# Crear la clase nodo
class node:
    # Crear el constructor de la clase
    def __init__(self, datoQueVieneDelMain = None, punteroQueVieneDelMain = None):
        self.data = str(datoQueVieneDelMain)
        self._next = punteroQueVieneDelMain
    
    # Método para visualizar la información
    def __str__(self):
        return self.data
    
class node2:
    # Crear el constructor de la clase
    def __init__(self, data1 = None, data2= None,  _next = None):
        self.data1 = str(data1)#Nombre de la persona
        self.data2 = str(data2)#Numero de Identifiacion
        self._next = _next
    
    # Método para viualizar la información
    def __str__(self):
        return self.data1 + ". ID: "+ self.data2
    
    