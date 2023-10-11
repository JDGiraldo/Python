#Crear la clase nodo
class node:
    #Crear el constructor de la clase
    def __init__(self, datoQueVieneDelMain = None, punteroQueVieneDelMain = None):
        self.data = str(datoQueVieneDelMain)
        self._next = punteroQueVieneDelMain

    #Metodo para visulizar la informacion
    def __str__(self):
        return self.data
#Creamos la segunda clase con varios datos en el nodo
class node2:
    def __init__(self, data1= None, data2 = None, _next= None):
        self.data1= data1
        self.data2= data2
        self._next= _next

    #Metodo para visualizar
    def __str__(self):
        return self.data1 + '. ID: '+ self.data2
